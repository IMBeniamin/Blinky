@echo off
setlocal
pushd %~dp0\..\
>nul 2>nul python --version
if errorlevel 1 goto ERR

:GOOD
python setup.py
goto EXIT_CLEAN
:ERR
echo Couldn't find python!
goto EXIT_CLEAN

:EXIT_CLEAN
popd
PAUSE

endlocal
