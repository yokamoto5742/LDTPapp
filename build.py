import subprocess
import shutil
from version_manager import update_version, update_main_py


def build_executable():
    # バージョンを更新
    new_version = update_version()
    update_main_py(new_version)

    subprocess.run([
        "pyinstaller",
        "--name=LDTPapp",
        "--windowed",
        "--icon=assets/LDPTapp_icon.ico",
        "main.py"
    ])

    # 必要なファイルをdistフォルダにコピー
    shutil.copy("config.ini", "dist/")
    shutil.copy("version.txt", "dist/")

    print(f"Executable built successfully. Version: {new_version}")


if __name__ == "__main__":
    build_executable()
