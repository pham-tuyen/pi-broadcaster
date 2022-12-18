import os, threading

download = threading.Thread(target=os.system, args=("python download.py", ))
play = threading.Thread(target=os.system, args=("python play.py", ))

download.start()
play.start()

download.join()
play.join()
