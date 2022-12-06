import re, os, json
from pytube import Playlist

f = open(".config", "r")
config = f.read()
config = json.loads(config)
f.close()

for i in range(0, len(config)):
    if not os.path.isdir(config[i]["dir"]):
        os.mkdir(config[i]["dir"])

playlist = Playlist(config[i]["url"])
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

for index in range(0, len(config)):
    for i in range(len(os.listdir(config[index]["dir"])), len(playlist.videos)):
        audioStream = playlist.videos[i].streams.get_by_itag("140")
        audioStream.download(output_path=config[index]["dir"], filename=str(i) + ".mp4")
        os.chdir(config[index]["dir"])  
        os.system("ffmpeg -i " + str(i) + ".mp4 " + str(i) + ".mp3")
        os.remove(str(i) + ".mp4")
        os.system("7z a " + str(i) + ".zip " + str(i) + ".mp3")
        os.remove(str(i) + ".mp3")
        os.chdir("..")