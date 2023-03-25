pyinstaller main.spec 
del releases\gongzone_launcher.exe /q
xcopy .\dist\gongzone_launcher.exe releases
rmdir /s/q .\dist 
rmdir /s/q .\build
pause