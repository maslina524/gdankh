import os
import platform
from pathlib import Path

def get_gd_appdata_path():
    os_name = platform.system()
    if os_name == 'Windows':
        return Path(os.environ.get('LOCALAPPDATA', '')) / 'GeometryDash'
    elif os_name == 'Darwin':
        return Path.home() / 'Library' / 'Application Support' / 'GeometryDash'