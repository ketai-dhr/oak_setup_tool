@echo off

%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d %~dp0
start .\depthai\depthai_demo_python\python.exe .\depthai\calibrate.py -s 2.5 -db -brd BW1098OBC

exit