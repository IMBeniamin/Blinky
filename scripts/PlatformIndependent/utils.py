import os
import subprocess
import shutil


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
