import os
import subprocess
import shutil
from enum import Enum
from importlib import import_module

from PlatformIndependent.pyValidation import PythonConfiguration as PythonRequirements


PythonRequirements.Validate()  # Check if all required packages are installed
colorama = import_module("colorama")
colorama.init()


class OutputLevel(Enum):
    def INFO(x): return print(colorama.Style.DIM +
                              "[INFO]" +
                              colorama.Style.BRIGHT +
                              f" {x}" +
                              colorama.Style.RESET_ALL)

    def WARNING(x): return print(colorama.Fore.YELLOW +
                                 "[WARNING]" +
                                 colorama.Fore.BLACK +
                                 colorama.Back.YELLOW +
                                 colorama.Style.DIM +
                                 f" {x}" +
                                 colorama.Style.RESET_ALL)

    def ERROR(x): return print(colorama.Fore.RED +
                               "[ERROR]" +
                               colorama.Fore.WHITE +
                               colorama.Back.RED +
                               colorama.Style.BRIGHT +
                               f" {x}" +
                               colorama.Style.RESET_ALL)

    def SUCCESS(x): return print(colorama.Fore.GREEN +
                                 "[SUCCESS]" +
                                 colorama.Fore.GREEN +
                                 colorama.Style.BRIGHT +
                                 f" {x}" +
                                 colorama.Style.RESET_ALL)

    def PROMPT(x): return print(colorama.Style.DIM +
                                colorama.Back.WHITE +
                                colorama.Fore.BLACK +
                                "[??]" +
                                colorama.Fore.MAGENTA +
                                colorama.Back.BLACK +
                                colorama.Style.BRIGHT +
                                f" {x}" +
                                colorama.Style.RESET_ALL)


def cprint(text: str, level=OutputLevel.INFO):
    level(text)


def pmk_system_choice():
    supported_systems = {
        "vs2022":  "Generate Visual Studio 2022 project files",
        "vs2019":  "Generate Visual Studio 2019 project files",
        "vs2017":  "Generate Visual Studio 2017 project files",
        "vs2015":  "Generate Visual Studio 2015 project files",
        "vs2013":  "Generate Visual Studio 2013 project files",
        "vs2012":  "Generate Visual Studio 2012 project files",
        "vs2010":  "Generate Visual Studio 2010 project files",
        "vs2008":  "Generate Visual Studio 2008 project files",
        "vs2005":  "Generate Visual Studio 2005 project files",
        "gmake":   "Generate GNU Makefiles(This generator is deprecated by gmake2)",
        "gmake2":  "Generate GNU Makefiles(including Cygwin and MinGW)",
        "xcode4":  "XCode projects",
        "codelite": "CodeLite projects"
    }
    map = {
        "h": lambda: [cprint(f"{colorama.Fore.CYAN}{k}{colorama.Style.RESET_ALL}: {v}", OutputLevel.INFO) for k, v in supported_systems.items()],
        "help": lambda: map["h"]
    }
    while True:
        cprint("\nWhat build system do you want to use?\n(h[elp] for a list of systems)...", OutputLevel.PROMPT)
        cmd = input("")
        try:
            map[cmd]()
        except KeyError:
            return cmd


def get_current_dir():
    return os.path.dirname(os.path.abspath(__file__))


def unzip_file(filepath, delete_zip=True):
    filepath = os.path.abspath(filepath)
    shutil.unpack_archive(filepath, os.path.dirname(filepath))
    os.remove(filepath) if delete_zip else None


def download_file(url, filepath):
    filepath = os.path.abspath(filepath)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    print(f"Downloading {url} to {filepath}")
    subprocess.Popen(["powershell", "wget", url, "-O",
                     filepath], stdout=subprocess.PIPE).communicate()


if __name__ == "__main__":
    print("Testing download function:")
    download_file(
        "http://ipv4.download.thinkbroadband.com/10MB.zip", "testFile")
