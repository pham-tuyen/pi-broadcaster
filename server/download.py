import re, os, json
from pytube import Playlist
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
        if item.endswith(".mp3") or item.endswith(".mp4"):
            os.remove(item)
    os.chdir("..")

while True:
    for index in range(0, len(config)):
        playlist = Playlist(config[index]["url"])
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        for i in range(len(os.listdir(config[index]["dir"])), len(playlist.videos)):
            audioStream = playlist.videos[i].streams.get_by_itag("140")
            audioStream.download(output_path=config[index]["dir"], filename=str(i) + ".mp4")
            os.chdir(config[index]["dir"])  
            os.system("ffmpeg -i " + str(i) + ".mp4 " + str(i) + ".mp3")
            os.remove(str(i) + ".mp4")
            os.system("7z a " + str(i) + ".zip " + str(i) + ".mp3")
            os.remove(str(i) + ".mp3")
            os.chdir("..")
            if datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second >= config[index]["time"] * 3600:
                break