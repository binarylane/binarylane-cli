@echo off

REM pyinstaller --paths is described as being like PYTHONPATH, but
REM it doesnt seem to function correctly when collecting submodules
REM so we will just set PYTHONPATH explicitly
set PYTHONPATH=src

echo from blcli import app ; app.main() > src\bl.py

FOR /F "tokens=*" %%g IN ('poetry version --short') do (set BLCLI_VERSION=%%g)
echo __version__ = '%BLCLI_VERSION%' > src\blcli\_version.py

poetry run pyinstaller -F --collect-submodules blcli src\bl.py --clean
del src\bl.py src\blcli\_version.py
