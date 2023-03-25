import os
import requests
from urllib.parse import urlparse
import pefile
print("########################################################")
print("####New Update Launcher####")
print("########################################################")
dir = '%s\\gongzone.exe'% os.path.expanduser("~")
def get_version_file ():
    try :
        pe = pefile.PE(dir)
        ProductVersionLS = pe.VS_FIXEDFILEINFO[0].ProductVersionLS
        ProductVersionMS = pe.VS_FIXEDFILEINFO[0].ProductVersionMS
        ProductVersion = (ProductVersionMS >> 16, ProductVersionMS & 0xFFFF, ProductVersionLS >> 16)
        pe.close()
        return 'v%s.%s.%s' % ProductVersion
    except:
        return 'v1.0.0 '

def get_version_git():
    r = requests.head("https://github.com/kimmoney/gongzone_releases/releases/latest")
    ver = r.headers['location'][-6:]
    return ver
print(dir)
ver_file = get_version_file()
ver_git  = get_version_git()
print("file:",ver_file)
print("git:",ver_git)

if ver_file == ver_git :
    print("open")
    pass
else:
    try:os.remove(dir)
    except:pass
    print("Installing new version")
    url = "https://github.com/kimmoney/gongzone_releases/releases/download/{}/gongzone_keep_point.exe".format(ver_git)
    file = requests.get(url,stream = True)
    print(url)
    parsed_file = urlparse(url)
    file_name = os.path.basename(parsed_file.path)
    file = requests.get(url)    
    open(dir, 'wb').write(file.content)
print('Finish')
commend = "start "+ dir
os.system(commend)