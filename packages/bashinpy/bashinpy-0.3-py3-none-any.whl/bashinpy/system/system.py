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

def cp(path1, path2):
    call(f"cp {path1} {path2}")
