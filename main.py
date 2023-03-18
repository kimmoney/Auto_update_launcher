import pefile

pe = pefile.PE(r'gongzone_keep_point.exe')

FileVersion = pe.FileInfo[0]#.StringTable[0].entries['FileVersion']
print(FileVersion)
