import os
import subprocess

class run:
    def exec(self, command):
        subprocess.run(["adb", "shell", command])

    def cmd(self, command):
        os.system(f"adb shell {command}")

    def push(self, system, device):
        os.system(f"adb push {system} {device}")

    def pull(self, device, system):
        os.system(f"adb pull {device} {system}")

class pm:
    def grant(self, package, permission):
        os.system(f"adb shell pm grant {package} android.permission.{permission}")

    def path(self, package):
        subprocess.run(["adb", "shell", "pm", "path", package])

    def clear(self, package):
        subprocess.run(["adb", "shell", "pm", "clear", package])

class screen:
    def cap(self, filename):
        subprocess.run(["adb", "shell", "screencap", filename])

    def record(self, filename):
        subprocess.run(["adb", "shell", "screenrecord", filename])

class apk:
    def install(self, path):
        subprocess.run(["adb", "install", path])

    def uninstall(self, path):
        subprocess.run(["adb", "uninstall", path])

    def logcat(self):
        subprocess.run(["adb", "logcat"])
