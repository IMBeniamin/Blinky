import os
from pathlib import Path

from PlatformIndependent import utils


class PremakeConfiguration:
    premakeVersion = "5.0.0-beta1"
    premakeZipUrls = f"https://github.com/premake/premake-core/releases/download/v{premakeVersion}/premake-{premakeVersion}-windows.zip"
    premakeLicenseUrl = "https://raw.githubusercontent.com/premake/premake-core/master/LICENSE.txt"
    premakeDirectory = "./vendor/premake/bin"

    @classmethod
    def Validate(cls):
        if (not cls.CheckIfPremakeInstalled()):
            utils.cprint("Premake is not installed.", utils.OutputLevel.ERROR)
            return False

        utils.cprint(
            f"Correct Premake located at {os.path.abspath(cls.premakeDirectory)}",
            utils.OutputLevel.SUCCESS)
        return True

    @classmethod
    def CheckIfPremakeInstalled(cls):
        premakeExe = Path(f"{cls.premakeDirectory}/premake5.exe")
        if (not premakeExe.exists()):
            return cls.InstallPremake()

        return True

    @classmethod
    def InstallPremake(cls):
        permissionGranted = False
        while not permissionGranted:
            reply = str(input(utils.colorama.Fore.MAGENTA +
                              "[PROMPT] " +
                              utils.colorama.Style.RESET_ALL +
                              utils.colorama.Fore.YELLOW +
                              "Premake not found. Would you like to download Premake {0:s}? [Y/N]: ".format(
                                  cls.premakeVersion) +
                              utils.colorama.Style.RESET_ALL)).lower().strip()[:1]
            if reply == 'n':
                return False
            permissionGranted = (reply == 'y')

        premakePath = f"{cls.premakeDirectory}/premake-{cls.premakeVersion}-windows.zip"
        utils.cprint("Downloading {0:s} to {1:s}".format(
            cls.premakeZipUrls, premakePath), utils.OutputLevel.INFO)
        utils.download_file(cls.premakeZipUrls, premakePath)
        utils.cprint("Extracting" + premakePath, utils.OutputLevel.INFO)
        utils.unzip_file(premakePath, delete_zip=True)
        utils.cprint(
            f"Premake {cls.premakeVersion} has been downloaded to '{cls.premakeDirectory}'",
            utils.OutputLevel.SUCCESS)

        premakeLicensePath = f"{cls.premakeDirectory}/LICENSE.txt"
        utils.cprint("Downloading {0:s} to {1:s}".format(
            cls.premakeLicenseUrl, premakeLicensePath), utils.OutputLevel.INFO)
        utils.download_file(cls.premakeLicenseUrl, premakeLicensePath)
        utils.cprint(
            f"Premake License file has been downloaded to '{cls.premakeDirectory}'",
            utils.OutputLevel.SUCCESS)

        return True
