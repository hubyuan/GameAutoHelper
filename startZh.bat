echo GameAutoHelper is going to run in 60 seconds, if you don't need it, close this cmd.
@echo off
timeout 60
rem �޸�GameAutoHelper ��·�����̷�
cd /D D:\code\GameAutoHelper
rem �޸�ҹ��ģ������·��
set emuPath=D:\soft\game\mumu\emulator\nemu\EmulatorShell
set emuPath1=D:\soft\game\mumu\emulator\nemu\vmonitor\bin

rem ��ҹ��ģ����
start "" "%emuPath%"\NemuPlayer.exe
timeout 120

rem ��
"%emuPath1%"\adb_server.exe connect 127.0.0.1:7555
timeout 10


rem ���ٻ���ϳ�
"%emuPath1%"\adb_server.exe -s 127.0.0.1:7555 shell input tap 422 278
timeout 120

rem ����
"%emuPath1%"\adb_server.exe -s 127.0.0.1:7555 shell input tap 1070 56
timeout 10

rem ����
"%emuPath1%"\adb_server.exe -s 127.0.0.1:7555 shell input tap 1070 56
timeout 10

python plan.py

timeout 10
rem �ر�ҹ��ģ����
taskkill /f /im NemuPlayer.exe

