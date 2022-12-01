from __future__ import unicode_literals
import os, time, json, platform
from datetime import datetime

f = open(".config", "r")
config = f.read()
config = json.loads(config)
f.close()

index = []
for i in range(0, len(config)):
    index.append(1)

while True:
    for i in range(0, len(config)):
        now = datetime.now()
        if now.hour * 3600 + now.minute * 60 + now.second <= config[i]["time"] * 3600:
            time.sleep(config[i]["time"] * 3600 - (now.hour * 3600 + now.minute * 60 + now.second))
            file = "\"" + os.listdir(config[i]["dir"])[len(os.listdir(config[i]["dir"])) - index[i]] + "\""
            os.chdir(config[i]["dir"])
            os.system("7z e " + file) 
            file = file.replace("zip", "mp3")
            os.system("mpg123 " + file)
            if platform.system() == "Windows": 
                os.system("del " + file)
            else:
                os.system("rm " + file)
            os.chdir("..")
            index[i] += 1
            if index[i] == len(os.listdir(config[i]["dir"])) + 1:
                index[i] = 1