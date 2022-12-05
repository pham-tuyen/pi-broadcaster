from __future__ import unicode_literals
import requests, youtube_dl, os, json, platform
from datetime import datetime

f = open(".config", "r")
config = f.read()
config = json.loads(config)
f.close()

for i in range(0, len(config)):
    if not os.path.isdir(config[i]["dir"]):
        os.mkdir(config[i]["dir"])

api = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&key=AIzaSyD9SzNDbCbjGG_S-3bVVHWHMjMq1qmfV9A&playlistId="
data = []
for i in range(0, len(config)):
    data.append(json.loads(requests.get(api + config[i]["id"]).text))

def download(id, name, dir):
    ytdl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': "/" + dir + "/" + name + ".%(ext)s"
    }
    try:
        with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
            ydl.download(["https://youtube.com/watch?v=" + id])
    except:
        pass
    if platform.system() == 'Windows':
        os.system("del " + dir + "/" + name + ".%(ext)s")
    else:
        os.system("rm " + dir + "/" + name + ".%(ext)s")
    os.system("7z a " + dir + "/" + name + ".zip " + dir + "/" + name + ".mp3")
    if platform.system() == 'Windows':
        os.system("del " + dir + "/" + name + ".mp3")
    else:
        os.system("rm " + dir + "/" + name + ".mp3")
    
while True:
    for i in range(0, len(config)):
        now = datetime.now()
        if now.hour * 3600 + now.minute * 60 + now.second <= config[i]["time"] * 3600:
            while True:
                download(data[i]["items"][len(os.listdir(config[i]["dir"]))]["snippet"]["resourceId"]["videoId"], str(len(os.listdir(config[i]["dir"]))), config[i]["dir"])
                now = datetime.now()
                if data[i]["nextPageToken"] == "" or now.hour * 3600 + now.minute * 60 + now.second >= config[i]["time"] * 3600:
                    break
                data[i] = json.loads(requests.get(api + config[i]["id"] + "&pageToken=" + data[i]["nextPageToken"]).text)
            