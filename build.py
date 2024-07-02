import subprocess
import shutil
import os
from version_manager import update_version, update_main_py


def build_executable():
    # バージョンを更新
    new_version = update_version()
    update_main_py(new_version)

    # PyInstallerでビルド
    subprocess.run(["pyinstaller", "--name=LDTPform", "--windowed", "--onefile", "main.py"])

    # 必要なファイルをdistフォルダにコピー
    shutil.copy("config.ini", "dist/")
    shutil.copy("version.txt", "dist/")

    # テンプレートファイルをdistフォルダにコピー
    if os.path.exists("template.xlsm"):
        shutil.copy("template.xlsm", "dist/")

    print(f"Executable built successfully. Version: {new_version}")


if __name__ == "__main__":
    build_executable()
