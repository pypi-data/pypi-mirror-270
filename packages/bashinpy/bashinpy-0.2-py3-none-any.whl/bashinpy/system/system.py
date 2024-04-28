import subprocess
import os

def call(command):
    parts = command.split()
    subprocess.run(parts)

def cmd(command):
    os.system(command)

def md(path):
    os.mkdir(path)

def cd(path):
    os.chdir(path)

