import os, time, json, platform
from datetime import datetime

f = open(".config", "r")
config = f.read()
config = json.loads(config)
f.close()

cache = open("cache", "r")
index_temp = cache.readlines()
cache.close()
if index_temp == []:
    fcache = open("cache", "w")
    fcache.write("0\n0\n0\n0")
    fcache.close()
cache = open("cache", "r")
index_temp = cache.readlines()
index = []
for i in range(0, len(index_temp)):
    index.append(int(index_temp[i]))
cache.close()

while True:
    for i in range(0, len(config)):
        now = datetime.now()
        if (now.hour * 3600 + now.minute * 60 + now.second <= config[i]["time"] * 3600) and (datetime.now().weekday() in config[i]["day"]):
            time.sleep(config[i]["time"] * 3600 - (now.hour * 3600 + now.minute * 60 + now.second))
            file = "\"" + os.listdir(config[i]["dir"])[index[i]] + "\""
            os.chdir(config[i]["dir"])
            os.system("unzip " + file) 
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
            fcache = open("cache", "w")
            for el in index:
                fcache.write(str(el) + "\n")
            fcache.close()