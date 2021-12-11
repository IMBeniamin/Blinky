import os
import subprocess
import shutil
from enum import Enum
from importlib import import_module
from PlatformIndependent.pyValidation import PythonConfiguration as PythonRequirements


PythonRequirements.Validate()
colorama = import_module("colorama")
colorama.init()


class OutputLevel(Enum):
    def INFO(x): return print(colorama.Fore.GREEN +
                              "[INFO] " +
                              colorama.Fore.WHITE +
                              colorama.Style.BRIGHT +
                              f"{x}" +
                              colorama.Style.RESET_ALL)

    def WARNING(x): return print(colorama.Fore.YELLOW +
                                 "[WARNING] " +
                                 colorama.Fore.BLACK +
                                 colorama.Back.YELLOW +
                                 colorama.Style.DIM +
                                 f"{x}" +
                                 colorama.Style.RESET_ALL)

    def ERROR(x): return print(colorama.Fore.RED +
                               "[ERROR] " +
                               colorama.Fore.WHITE +
                               colorama.Back.RED +
                               colorama.Style.BRIGHT +
                               f"{x}" +
                               colorama.Style.RESET_ALL)

    def SUCCESS(x): return print(colorama.Fore.GREEN +
                                 "[SUCCESS] " +
                                 colorama.Fore.GREEN +
                                 colorama.Style.BRIGHT +
                                 f"{x}" +
                                 colorama.Style.RESET_ALL)


def cprint(text: any, level=OutputLevel.INFO):
    level(text)


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
