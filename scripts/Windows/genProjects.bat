@echo off
pushd %~dp0\..\..\
set "version=vs2019"
set /P version="IDE to use [default: vs2019]: "
call vendor\premake\bin\premake5.exe %version%
popd