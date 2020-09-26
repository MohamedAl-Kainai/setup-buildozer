#! /usr/bin/python3
import os
from N4Tools import System,Design

commands = [
    'sudo apt-get install python3-setuptools',
    'apt list --upgradable',
    'sudo apt install git',
    'git clone https://github.com/kivy/buildozer.git',
    'cd buildozer && sudo python3 setup.py install',
    'sudo apt update',
    'sudo apt install -y git zip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev',
    'pip3 install --user --upgrade cython virtualenv',
    'sudo apt-get install cython',
    'python3 -m pip install cython',
]

os.chdir(os.environ['HOME'])
for i in commands:
    os.system(i)

Error = False
try:
    import Cython
except:
    Error = True
       
msg = 'GL## Done...'
if Error:msg = 'RL## Error...'
print(Design.Color.reader(msg))
