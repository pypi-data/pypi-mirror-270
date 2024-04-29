# update.py

import requests
import idaapi
from yaraforge.version import __version__

from yaraforge.utils.logger import get_global_logger

logger = get_global_logger()


def check_for_updates(force_check=False):
    try:
        # 檢查網路連接狀態
        if not is_network_available():
            if force_check:
                print("[YaraForge] No network connection. Update check skipped.")
            return

        print(f"[YaraForge] Current version: {__version__}")
        logger.info(f"Current version: {__version__}")

        # 從 PyPI 獲取最新版本號
        pypi_url = "https://pypi.org/pypi/yaraforge/json"
        response = requests.get(pypi_url)
        response.raise_for_status()
        latest_version = response.json()["info"]["version"]

        if latest_version > __version__:
            print(f"[YaraForge] New version available: {latest_version}")
            logger.info(f"New version available: {latest_version}")
            if idaapi.ask_yn(idaapi.ASKBTN_YES, f"A new version of YaraForge ({latest_version}) is available. Do you "
                                                f"want to update now?") == idaapi.ASKBTN_YES:
                perform_update()
            else:
                print("[YaraForge] You can update later by running the 'yf-update' command in the Python Console.")
        else:
            print("[YaraForge] No updates available.")
            logger.info("No updates available.")
    except requests.exceptions.RequestException as e:
        print(f"[YaraForge] Update check failed: {e}")
        logger.error(f"Update check failed: {e}")


def perform_update():
    try:
        # 獲取 IDA Pro 使用的 Python 解釋器路徑
        ida_python_path = idaapi.get_python_exe_path()

        # 使用 IDA Pro 的 Python 解釋器執行 pip 更新
        import subprocess
        subprocess.call([ida_python_path, "-m", "pip", "install", "--upgrade", "yaraforge"])
        print("[YaraForge] Update completed. Please restart IDA Pro for the changes to take effect.")
        logger.info("Update completed. Please restart IDA Pro for the changes to take effect.")
    except Exception as e:
        print(f"[YaraForge] Update failed: {e}")
        logger.error(f"Update failed: {e}")


def is_network_available():
    import socket
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
