@echo off

start .\depthai\depthai_demo_python\python.exe .\depthai\depthai_demo_python\get-pip.py

ping /n 10 127.0.0.1 > nul

start .\depthai\depthai_demo_python\python.exe -m pip install -e .\depthai\depthai_sdk

start .\python\python.exe .\depthai\depthai_demo_python\get-pip.py

start .\python\python.exe -m pip install -e .\depthai\depthai_sdk

exit