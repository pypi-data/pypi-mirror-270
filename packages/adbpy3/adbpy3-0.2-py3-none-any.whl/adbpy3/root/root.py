import os

class shell:
    def on(self):
        os.system("adb root")

    def off(self):
        os.system("adb unroot")
