import os
import subprocess

class run:
    def exec(command):
        subprocess.run(["adb", "shell", command])

    def cmd(command):
        os.system(f"adb shell {command}")

    def push(system, device):
        os.system(f"adb push {system} {device}")

    def pull(device, system):
        os.system(f"adb pull {device} {system}")

class pm:
    def grant(package, permission):
        os.system(f"adb shell pm grant {package} android.permission.{permmision}")

    def path(package):
        subprocess.run(["adb", "shell", "pm", "path", package])

    def clear(package):
        subprocess.run(["adb", "shell", "pm", "clear", package])

class screen:
    def cap(filename):
        subprocess.run(["adb", "shell", "screencap", filename])

    def record(filename):
        subprocess.run(["adb", "shell", "screenrecord", filename])

class apk:
    def install(path):
        subprocess.run(["adb", "install", path])

    def uninstall(path):
        subprocess.run(["adb", "uninstall", path])

    def logcat():
        subprocess.run(["adb", "logcat"])
