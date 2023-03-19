import os
import requests
from urllib.parse import urlparse
from win32api import GetFileVersionInfo, LOWORD, HIWORD

def get_version_file ():
    info = GetFileVersionInfo ('gongzone_keep_point.exe', "\\")
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    print("v{}.{}.{}".format(HIWORD (ms), LOWORD (ms), HIWORD (ls)))
    return "v{}.{}.{}".format(HIWORD (ms), LOWORD (ms), HIWORD (ls))
def get_version_git():
    r = requests.head("https://github.com/kimmoney/gongzone_releases/releases/latest")
    ver = r.headers['location'][-6:]
    return ver
ver_file = get_version_file()
ver_git  = get_version_git()
print("file:",ver_file)
print("git:",ver_git)
if ver_file == ver_git :
    print("open")
    pass
else:
    print()
    url = "https://github.com/kimmoney/gongzone_releases/releases/download/{}/gongzone_keep_point.exe".format(ver_git)
    file = requests.get(url,stream = True)
    parsed_file = urlparse(url)
    file_name = os.path.basename(parsed_file.path)
    file = requests.get(url)
    open('gongzone_keep_point.exe', 'wb').write(file.content)