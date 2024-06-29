import os
import subprocess
import sys


def restart_app():
    if getattr(sys, 'frozen', False):
        # アプリケーションが実行可能ファイルとして実行されている場合
        application_path = sys.executable
    else:
        # スクリプトとして実行されている場合
        application_path = sys.executable
        script_path = os.path.abspath(sys.argv[0])

    # 新しいプロセスを開始
    if getattr(sys, 'frozen', False):
        subprocess.Popen([application_path])
    else:
        subprocess.Popen([application_path, script_path])


if __name__ == "__main__":
    restart_app()
