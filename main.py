import os
import requests
from urllib.parse import urlparse
from win32api import GetFileVersionInfo, LOWORD, HIWORD

def get_version_git ():
    info = GetFileVersionInfo ('gongzone_keep_point.exe', "\\")
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)

r = requests.head("https://github.com/kimmoney/gongzone_releases/releases/latest")
ver = r.headers['location'][-6:]
if ver == get_version_git() :
    pass
else:
    url = "https://github.com/kimmoney/gongzone_releases/releases/download/{}/gongzone_keep_point.exe".format(ver)
    file = requests.get(url,stream = True)
    parsed_file = urlparse(url)
    file_name = os.path.basename(parsed_file.path)
    file = requests.get(url)
    open('C:/gongzone_keep_point.exe', 'wb').write(file.content)