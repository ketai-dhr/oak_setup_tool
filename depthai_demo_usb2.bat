@echo off

%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d %~dp0
start .\depthai\depthai_demo_python\python.exe .\depthai\depthai_demo.py -gt cv -usbs usb2

exit