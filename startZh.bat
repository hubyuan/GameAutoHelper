echo GameAutoHelper is going to run in 60 seconds, if you don't need it, close this cmd.
@echo off
timeout 60
rem 修改GameAutoHelper 的路径和盘符
cd /D D:\code\GameAutoHelper
rem 修改夜神模拟器的路径
set emuPath=D:\soft\game\mumu\emulator\nemu\EmulatorShell
set emuPath1=D:\soft\game\mumu\emulator\nemu\vmonitor\bin

rem 打开夜神模拟器
start "" "%emuPath%"\NemuPlayer.exe
timeout 120

rem 打开
"%emuPath1%"\adb_server.exe connect 127.0.0.1:7555
timeout 10


rem 打开召唤与合成
"%emuPath1%"\adb_server.exe -s 127.0.0.1:7555 shell input tap 422 278
timeout 120

rem 进入
"%emuPath1%"\adb_server.exe -s 127.0.0.1:7555 shell input tap 1070 56
timeout 10

rem 进入
"%emuPath1%"\adb_server.exe -s 127.0.0.1:7555 shell input tap 1070 56
timeout 10

python plan.py

timeout 10
rem 关闭夜神模拟器
taskkill /f /im NemuPlayer.exe

