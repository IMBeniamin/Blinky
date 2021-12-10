import os
import subprocess
import platform
from importlib import import_module

from PlatformIndependent.pyValidation import PythonConfiguration as PythonRequirements

userPlatform = platform.system()
premakeValidation = import_module(".premakeValidation", userPlatform)

# Make sure everything we need for the setup is installed
PythonRequirements.Validate()

os.chdir('./../')  # Change from devtools/scripts directory to root

# Initialize all dependencies

premakeInstalled = premakeValidation.PremakeConfiguration.Validate()

# Update submodules and building the project

print("\nUpdating submodules...")
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])

if (premakeInstalled):
    if platform.system() == "Windows":
        print("\nRunning premake...")
        subprocess.call([os.path.abspath(f"./scripts/{userPlatform}/genProjects.bat"), "nopause"])

    print("\nSetup completed!")
else:
    print("Hazel requires Premake to generate project files.")
