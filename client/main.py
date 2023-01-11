import eel, threading, os, eel
from hashlib import sha256

eel.init("src")
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')

def start():
    eel.start('app.html', mode='electron')

def back():
    os.system("net stop winnat")
    os.system("net start winnat")
    os.system("npm run dev")

electron = threading.Thread(target=start, args=())
vite = threading.Thread(target=back, args=())
vite.start()
electron.start()
vite.join()
electron.join()



