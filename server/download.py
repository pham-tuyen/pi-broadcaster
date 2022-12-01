from __future__ import unicode_literals
import requests, youtube_dl, os, json, platform
from datetime import datetime

f = open(".config", "r")
config = f.read()
config = json.loads(config)
f.close()

for i in range(0, len(config)):
    os.mkdir(config[i]["dir"])

data = []
for i in range(0, len(config)):
    data.append(json.loads(requests.get(config[i]["link"]).text))

index = []
for i in range(0, len(config)):
    index.append(len(os.listdir(config[i]["dir"])))

def download(id, name):
    ytdl_opts = {
        'outtmpl': name + ".mp4"
    }
    try:
        with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
            ydl.download(["https://youtube.com/watch?v=" + id])
    except:
        pass
    os.system("ffmpeg -i " + name + ".mp4 " + name + ".mp3")
    if platform.system() == 'Windows':
        os.system("del " + name + ".mp4")
    else:
        os.system("rm " + name + ".mp4")
    os.system("7z a " + name + ".zip " + name + ".mp3")
    if platform.system() == 'Windows':
        os.system("del " + name + ".mp3")
    else:
        os.system("rm " + name + ".mp3")
    
while True:
    for i in range(0, len(config)):
        now = datetime.now()
        if now.hour * 3600 + now.minute * 60 + now.second <= config[i]["time"] * 3600:
            while True:
                download(data[i]["items"][index]["snippet"]["resourceId"]["videoId"])
                now = datetime.now()
                if data[i]["nextPageToken"] == "" or now.hour * 3600 + now.minute * 60 + now.second >= config[i]["time"] * 3600:
                    break
                                   