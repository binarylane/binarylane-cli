@echo off

REM pyinstaller --paths is described as being like PYTHONPATH, but
REM it doesnt seem to function correctly when collecting submodules
REM so we will just set PYTHONPATH explicitly
set PYTHONPATH=src

echo from blcli import app ; app.main() > src\bl.py
pyinstaller -F --collect-submodules blcli src\bl.py --clean
del src\bl.py
