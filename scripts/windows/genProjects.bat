@echo off
pushd %~dp0\..\
set "UserInputPath=vs2022"
set /P UserInputPath="IDE in use(enter=vs2022): "
echo you wrote %UserInputPath%
call vendor\premake\bin\premake5.exe %UserInputPath%
popd
PAUSE
