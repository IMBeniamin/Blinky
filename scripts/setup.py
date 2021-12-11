import os
import subprocess
import platform
from importlib import import_module
from PlatformIndependent.utils import cprint, OutputLevel

userPlatform = platform.system()
premakeValidation = import_module(".premakeValidation", userPlatform)

os.chdir('./../')  # Change from devtools/scripts directory to root

# Initialize all dependencies

premakeInstalled = premakeValidation.PremakeConfiguration.Validate()

# Update submodules and building the project

cprint("Updating submodules...", OutputLevel.INFO)
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])

if (premakeInstalled):
    if platform.system() == "Windows":
        cprint("Running premake...", OutputLevel.INFO)
        cprint("--------------------PREMAKE--------------------", OutputLevel.INFO)
        subprocess.call(
            [os.path.abspath(f"./scripts/{userPlatform}/genProjects.bat"), "nopause"])
    cprint("--------------------/PREMAKE--------------------", OutputLevel.INFO)
    cprint("Setup completed!", OutputLevel.SUCCESS)
else:
    cprint("Bilnky requires Premake to generate project files.", OutputLevel.ERROR)
