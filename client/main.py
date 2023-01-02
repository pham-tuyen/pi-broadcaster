import eel, threading, os, eel.browsers, time, sys

eel.init("src")
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')

def close_callback(route, websockets):
    if not websockets:
        os.system("taskkill /im node.exe /F")
        sys.exit()

def start():
    time.sleep(3) 
    eel.start('app.html', mode='electron', close_callback=close_callback)

def back():
    os.system("net stop winnat")
    os.system("net start winnat")
    os.system("npm run preview")

electron = threading.Thread(target=start, args=())
vite = threading.Thread(target=back, args=())
vite.start()
electron.start()
vite.join()
electron.join()



