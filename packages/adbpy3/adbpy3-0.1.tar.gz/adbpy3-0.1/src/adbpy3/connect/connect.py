import os
import subprocess

def start(ip):
    subprocess.run(["adb", "connect", ip])

def stop():
    os.system("adb disconnect")
