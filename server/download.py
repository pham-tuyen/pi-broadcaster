import os, json
from datetime import datetime

f = open(".config", "r")
config = f.read()
config = json.loads(config)
f.close()

for i in range(0, len(config)):
    if not os.path.isdir(config[i]["dir"]):
        os.mkdir(config[i]["dir"])
    os.chdir(config[i]["dir"])
    for item in os.listdir("."):
        if item.endswith(".mp3") or item.endswith(".webm") or item.endswith(".part"):
            os.remove(item)
    os.chdir("..")

while True:
    for index in range(0, len(config)):
        if datetime.now().weekday() in config[index]["day"] and 0 == os.system('ping finxter.com -w 4 > clear'):
            playlist = os.popen("youtube-dl -j --flat-playlist " + config[index]["id"]).read()
            data = json.loads("[" +  playlist.replace("\n", ",")[0:len(playlist.replace("\n", ",")) - 1] + "]")
            for i in range(len(os.listdir(config[index]["dir"])), len(data)):
                command = "youtube-dl -i --extract-audio --audio-format mp3 -o \"" + config[index]["dir"] + "/" + str(len(os.listdir(config[index]["dir"]))) + ".%(ext)s\" https://youtube.com/watch?v=" + data[i]["id"]
                print(command)
                os.system(command)
                os.chdir(config[index]["dir"])  
                try:
                    os.system("zip " + str(i) + ".zip " + str(i) + ".mp3")
                    os.remove(str(i) + ".mp3")
                except:
                    pass
                os.chdir("..")
                if datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second >= config[index]["time"] * 3600:
                    break
                
                
        

      