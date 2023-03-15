"""Generate updated API bindings and CLI commands from OpenAPI specification document"""
from __future__ import annotations

import shutil
import subprocess
import textwrap
import urllib.error
import urllib.request
from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence


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
        """
            )
        )
    subprocess.check_call(["openapi-python-client", "update", "--path", openapi_path, "--config", config_path])

    # lib/binarylane needs to be a namespace package
    (lib_package / "__init__.py").unlink()

    # The generated models package init imports all models, which takes too long for short-lived CLI process
    (lib_package / "models" / "__init__.py").write_text("")

    # Use absolute imports and import __future__annotations
    # Cannot check for returncode 0 as these tools return non-zero when a file is modified
    lib_modules = list(map(str, lib_package.rglob("*.py")))
    subprocess.call(["absolufy-imports", "--application-directories", "lib"] + lib_modules)
    subprocess.call(["isort", "--quiet", "--add-import", "from __future__ import annotations"] + lib_modules)


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
    request = parser.parse_args(args)

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
