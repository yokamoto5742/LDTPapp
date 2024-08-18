import subprocess
import shutil
import os
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
    shutil.copy("config.ini", "dist/LDTPapp")
    shutil.copy("version.txt", "dist/LDTPapp")
    excel_src = r"C:\Shinseikai\LDTPapp\LDTPform.xlsm"
    excel_dst = os.path.join("dist/LDTPapp", "LDTPform.xlsm")
    shutil.copy(excel_src, excel_dst)

    print(f"Executable built successfully. Version: {new_version}")
    print(f"Excel file copied to: {excel_dst}")


if __name__ == "__main__":
    build_executable()
