@echo off

pip install . -t exe

REM pyinstaller --paths is described as being like PYTHONPATH, but
REM it doesnt seem to function correctly when collecting submodules
REM so we will just set PYTHONPATH explicitly
set PYTHONPATH=exe

echo from blcli import app ; app.main() > exe\bl.py

FOR /F "tokens=*" %%g IN ('poetry version --short') do (set BLCLI_VERSION=%%g)
echo __version__ = '%BLCLI_VERSION%' > exe\blcli\_version.py

pyinstaller -F --collect-submodules blcli exe\bl.py --clean
rmdir /s /q exe
