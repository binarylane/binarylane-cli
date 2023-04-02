"""Generate updated API bindings and CLI commands from OpenAPI specification document"""
from __future__ import annotations

import re
import shutil
import subprocess
import textwrap
import urllib.error
import urllib.request
from argparse import SUPPRESS, ArgumentParser
from pathlib import Path
from typing import List, Optional, Sequence


def mkempty(directory: Path) -> None:
    """Create `directory` if it does not already exist, and remove all files and subdirectories if it does."""
    if directory.exists():
        if not directory.is_dir():
            raise ValueError(f"{directory} is not a directory")
        shutil.rmtree(directory)
    directory.mkdir()


def generate_library(temp_dir: Path, openapi_path: Path) -> None:
    """Use openapi-python-client to update API bindings in lib/binarylane"""
    lib_dir = get_project_dir() / "lib"
    lib_package = lib_dir / "binarylane"
    mkempty(lib_package)

    # Create config.yml for openapi-python-client and update package
    config_path = temp_dir / "config.yml"
    with open(config_path, "w") as file:
        file.write(
            textwrap.dedent(
                f"""\
            project_name_override: {lib_dir}
            package_name_override: {lib_package.name}

            # Additional post-hooks are used to remove openapi-python-client's use of "lazy" imports
            post_hooks:
              # Convert openapi-python-client generated models to use eager import
              - python ../scripts/generate.py --library-eager-imports
              # absolufy-imports seems to require isort to be used first
              - isort --add-import "from __future__ import annotations" .
              # absolufy-imports cannot recurse on its own, so we do that via generate.py
              - python ../scripts/generate.py --library-absolufy-imports
              # Finally, call the standard openapi-python-client post hooks
              - autoflake -i -r --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports .
              - isort .
              - black .
        """
            )
        )
    subprocess.check_call(["openapi-python-client", "update", "--path", openapi_path, "--config", config_path])

    # lib/binarylane needs to be a namespace package
    (lib_package / "__init__.py").unlink()

    # The generated models package init imports all models, which takes too long for short-lived CLI process
    (lib_package / "models" / "__init__.py").write_text("")


def library_eager_imports() -> None:
    """
    Convert openapi-python-client "lazy" imports to "eager" (normal) imports

    openapi-python-client uses `if TYPE_CHECKING:` to avoid importing other models at runtime, but we need those
    types to be loaded so that when binarylane.console.parser.formatter calls typing.get_type_hints(),
    get_type_hints() can resolve the relevant types at runtime
    """

    import_pattern = re.compile("^\\s+from .* import (.*)")
    docstring_pattern = re.compile(r"^\s*(" + r'"""[^"]*(?!""")|' + r"'''[^'](?!''')" + r")")  # start/end but not both
    for module in Path.cwd().rglob("*.py"):

        # Read module source code lines into a list
        with open(module, "rt") as file:
            lines = file.readlines()

        # scan through the lines for `IF TYPE_CHECKING:` and once found, dedent the subsequent from+import lines
        # We also convert ForwardRef type annotations to standard annotations and remove non-toplevel imports
        dedent_imports = False
        docstring_block = False
        forwardref_types: List[str] = []
        for line_number, line in enumerate(lines):
            new_value: Optional[str] = line[:-1]
            indented_import = import_pattern.match(line)
            if docstring_pattern.match(line):
                docstring_block = not docstring_block

            # Remove type-checking line and set bool to dedent its imports
            if line == "if TYPE_CHECKING:\n":
                new_value = None
                dedent_imports = True
            # If dedent_imports is enabled, but this line is not an import we are finished dedenting the block
            elif dedent_imports and not indented_import:
                dedent_imports = False
            # If dedent_imports is enabled, and this is an import from that block; dedent it
            elif dedent_imports and not docstring_block and indented_import:
                forwardref_types += list(map(str.strip, indented_import.group(1).split(",")))
                new_value = textwrap.dedent(line)
            # If this import is indented outside of the TYPE_CHECKING, its an unnecessary import within a function
            elif not dedent_imports and indented_import:
                new_value = None

            # Perform any ForwardRef fixups that this line requires
            pre_forwardref_fixup = new_value
            if new_value is not None:
                for type_ in forwardref_types:
                    new_value = new_value.replace(f'"{type_}"', type_).replace(f"'{type_}'", type_)

            # Removing forwardref from docstring will shorten the line, and potentially allow another word if
            # the attribute description was long enough to wrap. We fix that up for so that `git diff` will
            # exactly match the previous implementation.

            # If we are changing this line, we are in a docstring and this line is an attribute: description
            if new_value and pre_forwardref_fixup != new_value and docstring_block and re.search(": .", line):

                # Grab the next line and remove newline
                next_line = lines[line_number + 1][:-1]

                # If next line isnt end of the docstring block, and looks like a wrapped description
                if not docstring_pattern.match(next_line) and re.match(r"^\s+[a-zA-Z]([^:]+)$", next_line):

                    # Remove and store the whitespace indentation from next_line for use later
                    indentation = ""
                    while next_line[0] == " ":
                        indentation += " "
                        next_line = next_line[1:]

                    LINE_LENGTH = 120
                    # While our current line is under-length, and there's words left in the next line
                    while len(new_value) <= LINE_LENGTH and " " in next_line:
                        # Split a word off
                        word, remainder = next_line.split(" ", 1)
                        # If the next word will make the current line too long, we are done
                        if len(new_value) + len(word) + 1 > LINE_LENGTH:
                            break
                        # Add word to current line, and remove it from next line.
                        new_value += f" {word}"
                        next_line = remainder

                    # All done, put newlines back and update lines[] with the shortened next line
                    lines[line_number + 1] = indentation + next_line + "\n"

            # Store whatever modifications we made to the line
            new_value = new_value + "\n" if new_value is not None else ""
            lines[line_number] = new_value

        # Write our modified module back to disk
        with open(module, "wt") as file:
            file.writelines(lines)


def library_absolufy_imports() -> None:
    """
    Convert relative imports within openapi-python-client generated library to absolute.

    This implementation uses absolufy-imports which does not support recursing into a directory. It must be supplied
    with a list of files to fix, so we generate that list via rglob() and call absolufy-imports.
    """
    lib_modules = list(map(str, Path.cwd().rglob("*.py")))
    subprocess.call(["absolufy-imports", "--application-directories", "."] + lib_modules)


def generate_commands(temp_dir: Path, openapi_path: Path) -> None:
    """Use openapi-python-client with custom templates to update API command runners"""
    build_dir = temp_dir
    build_package = build_dir / "commands"
    build_package.mkdir()

    # Create config.yml for openapi-python-client and build package to temporary directory
    templates_dir = get_project_dir() / "templates"
    config_path = temp_dir / "config.yml"
    with open(config_path, "w") as file:
        file.write(
            textwrap.dedent(
                f"""\
                project_name_override: {build_dir}
                package_name_override: {build_package.name}
            """
            )
        )
    subprocess.check_call(
        [
            "openapi-python-client",
            "update",
            "--path",
            openapi_path,
            "--config",
            config_path,
            "--custom-template-path",
            templates_dir,
        ]
    )

    # Move the "api" package (discarding the models, etc) from temporary directory
    # to the correct location for commands package in our source tree
    commands_dir = get_project_dir() / "src" / "binarylane" / "console" / "commands" / "api"
    mkempty(commands_dir)

    # Move the generated api/__init__.py to our directory
    build_package /= "api"
    (build_package / "__init__.py").rename(commands_dir / "__init__.py")

    # Now combine the api/$tag/$operation.py files into a single directory
    for module in build_package.glob("*/*.py"):
        if module.name == "__init__.py":
            continue
        if (commands_dir / module.name).exists():
            raise RuntimeError(f"Module name {module.name} conflict")
        module.rename(commands_dir / module.name)


def get_project_dir() -> Path:
    """Get path to root of project working tree"""
    result = Path(__file__).absolute().parents[1]
    project_toml = result / "pyproject.toml"
    if not project_toml.is_file():
        raise EnvironmentError(f"{result} does not contain pyproject.toml?")
    return result


def download_openapi_spec(url: str, output: Path) -> None:
    with urllib.request.urlopen(url) as response:
        output.write_bytes(response.read())


def main(args: Sequence[str]) -> None:
    """Command-line entrypoint"""

    openapi_url = "https://api.binarylane.com.au/reference/openapi.json"

    parser = ArgumentParser()
    parser.add_argument(
        "--generator",
        metavar="NAME",
        default="openapi-python-client",
        help=f"Path to openapi-python-client executable (Default: '%(default)s')",
    )
    parser.add_argument(
        "--url",
        dest="openapi_url",
        metavar="URL",
        help=f"Download OpenAPI specification from %(metavar)s (Default: '%(default)s')",
        default=openapi_url,
    )
    parser.add_argument(
        "--file",
        dest="openapi_file",
        metavar="FILE",
        help=f"Use local OpenAPI specification at %(metavar)s instead of downloading it from URL",
    )

    only = parser.add_mutually_exclusive_group()
    only.add_argument("--library", default=False, action="store_true", help="Generate 'lib/binarylane' only")
    only.add_argument(
        "--commands", default=False, action="store_true", help="Generate 'src/binarylane/console/commands' only"
    )
    only.add_argument("--library-eager-imports", default=False, action="store_true", help=SUPPRESS)
    only.add_argument("--library-absolufy-imports", default=False, action="store_true", help=SUPPRESS)
    request = parser.parse_args(args)

    # This is called by --library to convert the generated library from lazy import to eager
    if request.library_eager_imports:
        library_eager_imports()
        return

    # This is called by --library to convert the generated library imports from relative to absolute
    if request.library_absolufy_imports:
        library_absolufy_imports()
        return

    # Enable both if a specific part was not requested
    if not (request.library or request.commands):
        request.library = True
        request.commands = True

    # Create a temporary directory for use during generation
    generate_dir = get_project_dir() / "_generate"
    mkempty(generate_dir)

    # Generate code as requested:
    try:
        # Download spec if requested, and store a copy in openapi_path
        if not request.openapi_file:
            openapi_path = generate_dir / "openapi.json"
            try:
                download_openapi_spec(request.openapi_url, openapi_path)
            except urllib.error.HTTPError as exc:
                parser.error(f"{request.openapi_url} - {exc.code} {exc.reason}")
        # Otherwise, verify the specified file exists
        else:
            openapi_path = Path(request.openapi_file)
            if not openapi_path.is_file():
                parser.error(f"{request.openapi_file} not found")

        # Generate the requested part(s)
        if request.library:
            generate_library(temp_dir=generate_dir, openapi_path=openapi_path)
        if request.commands:
            generate_commands(temp_dir=generate_dir, openapi_path=openapi_path)

    # Cleanup
    finally:
        shutil.rmtree(generate_dir)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
