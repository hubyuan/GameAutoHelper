echo GameAutoHelper is going to run in 60 seconds, if you don't need it, close this cmd.
@echo off
timeout 1



set emuPath1=D:\soft\platform-tools


rem ´ò¿ª
"%emuPath1%"\adb.exe -s 2ba69e8c shell input tap 175 725
timeout 1
"%emuPath1%"\adb.exe -s 2ba69e8c shell input tap 175 725
timeout 10

echo 111


