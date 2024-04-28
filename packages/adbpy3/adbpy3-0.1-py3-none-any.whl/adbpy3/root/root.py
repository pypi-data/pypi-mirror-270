import os

class shell:
    def on():
        os.system("adb root")

    def off():
        os.system("adb unroot")
