import os
import subprocess
import platform
from importlib import import_module

from PlatformIndependent.utils import cprint, OutputLevel, pmk_system_choice  # Automatically checks if require packages are installed and if not installs them

userPlatform = platform.system()
# Automatically tries to load the correct module for the current platform
# For each platform, there should exist a folder with its name that contains all necessary validation code
premakeValidation = import_module(".premakeValidation", userPlatform)

os.chdir('./../')  # Change from scripts directory to root

# Initialize all dependencies

premakeInstalled = premakeValidation.PremakeConfiguration.Validate()

# Update submodules and building the project

cprint("Updating submodules...", OutputLevel.INFO)
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])

if (premakeInstalled):
    if platform.system() == "Windows":
        cprint("Running premake...", OutputLevel.INFO)
        cprint("--------------------PREMAKE--------------------", OutputLevel.INFO)
        ret_code = subprocess.call([os.path.abspath(f"vendor/premake/bin/premake5.exe"), pmk_system_choice()])
        cprint("--------------------/PREMAKE--------------------", OutputLevel.INFO)
        if not ret_code:
            cprint("Setup completed!", OutputLevel.SUCCESS)
        else:
            cprint("Setup failed!", OutputLevel.ERROR)
    else:
        cprint("Cannot run premake on this platform", OutputLevel.ERROR)
else:
    cprint("Bilnky requires Premake to generate project files.", OutputLevel.ERROR)
