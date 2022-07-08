import os
import sys
import shutil
import zipfile
import subprocess

path = sys.path[0]
target_dir = path + r'/depthai-experiments'


def findName(i, file_name):
    if file_name not in i:
        target_dir_new = target_dir + '/' + i
        try:
            shutil.rmtree(target_dir_new)
        except OSError:
            pass


def delete(dir, filename):
    for file in os.listdir(dir):
        findName(file, filename)


def sh(pwd, shell=True):
    subprocess.check_call(pwd, shell)


def search(findStr):
    if "." in findStr:
        search = os.path.isfile(findStr)
    else:
        search = os.path.isdir(findStr)
    return search


search_experiments = search(target_dir)
if (1 == search_experiments):
    delete(target_dir, "gen2")
elif (0 == search_experiments):
    sh("git clone https://gitee.com/oakchina/depthai-experiments.git")
    delete(target_dir, "gen2")

depthai_path = path + r"/depthai"
search_depthai = search(depthai_path)
if (1 == search_depthai):
    pass
else:
    sh("git clone https://gitee.com/oakchina/depthai.git")

search_python = search("python")
search_python_zip = search("python.zip")
if (0 == search_python):
    if (1 == search_python_zip):
        print("Start unzipping python, please wait")
        f = zipfile.ZipFile('python.zip')
        for file in f.namelist():
            f.extract(file, r'.')
        print("Unzip python complete")
        f.close()
    else:
        print("download at address: http://192.168.0.48:8081/test/oak_setup_tools/uploads/d214060b729b050cefea9d559852917e/python.zip and put it in the home directory")

search_depthai_python_realpath = path + "/depthai/depthai_demo_python"
search_depthai_python = search(search_depthai_python_realpath)
search_depthai_python_zip = search("depthai_demo_python.zip")
if (0 == search_depthai_python):
    if (1 == search_depthai_python_zip):
        print("Start unzipping depthai_demo_python, please wait")
        f_ = zipfile.ZipFile('depthai_demo_python.zip')
        for file in f_.namelist():
            f_.extract(file, r'./depthai/')
        print("Unzip python complete")
        f_.close()
        try:
            sh(".\depthai\depthai_demo_python\python.exe .\depthai\install_requirements.py")
        except:
            pass
    else:
        print("download at address: http://192.168.0.48:8081/test/oak_setup_tools/uploads/cbdb5e63229d20a4d8001585c4579eac/depthai_demo_python.zip and put it in the home directory")
elif (1 == search_depthai_python):
    try:
        sh(".\depthai\depthai_demo_python\python.exe .\depthai\install_requirements.py")
    except:
        pass

depthai_python_path = path + r"/depthai-python"
depthai_API_examples_path = path + r"/depthai_API_examples"
search_depthai_python_path = search(depthai_python_path)
search_depthai_API_examples_path = search(depthai_API_examples_path)
search_python_again = search("python")
move_depthai_python_path = depthai_python_path + "/examples"
examples_path = path + r"/examples"

if (0 == search_depthai_python_path and 0 == search_depthai_API_examples_path):
    sh("git clone https://gitee.com/oakchina/depthai-python.git")
    if (1 == search_python_again):
        try:
            sh(".\python\python.exe .\depthai_API_examples\install_requirements.py")
        except:
            pass
        shutil.move(move_depthai_python_path, path)
        os.rename(examples_path, depthai_API_examples_path)
    else:
        print("Please build the python environment first")
elif (1 == search_depthai_python_path and 0 == search_depthai_API_examples_path):
    if (1 == search_python_again):
        try:
            sh(".\python\python.exe .\depthai_API_examples\install_requirements.py")
        except:
            pass
        shutil.move(move_depthai_python_path, path)
        os.rename(examples_path, depthai_API_examples_path)
    else:
        print("Please build the python environment first")
elif (0 == search_depthai_python_path and 1 == search_depthai_API_examples_path):
    if (1 == search_python_again):
        try:
            sh(".\python\python.exe .\depthai_API_examples\install_requirements.py")
        except:
            pass
        # shutil.move(move_depthai_python_path, path)
        # os.rename(examples_path, depthai_API_examples_path)
    else:
        print("Please build the python environment first")

elif (1 == search_depthai_python_path and 1 == search_depthai_API_examples_path):
    if (1 == search_python_again):
        try:
            sh(".\python\python.exe .\depthai_API_examples\install_requirements.py")
        except:
            pass
        # shutil.move(move_depthai_python_path, path)
        # os.rename(examples_path, depthai_API_examples_path)
    else:
        print("Please build the python environment first")
