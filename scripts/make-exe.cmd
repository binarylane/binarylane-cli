@echo off

pip install . -t exe

REM pyinstaller --paths is described as being like PYTHONPATH, but
REM it doesnt seem to function correctly when collecting submodules
REM so we will just set PYTHONPATH explicitly
set PYTHONPATH=exe

echo from binarylane.console import app ; app.main() > exe\bl.py

REM I believe this is required because pyinstaller bundle does not contain "installed"
REM packages, instead it is a "raw" bundle of the required modules.
FOR /F "tokens=*" %%g IN ('poetry version --short') do (set PROJECT_VERSION=%%g)
echo __version__ = '%PROJECT_VERSION%' > exe\binarylane\console\_version.py

pyinstaller --name bl --onefile --collect-submodules binarylane exe\bl.py --clean
rmdir /s /q exe
