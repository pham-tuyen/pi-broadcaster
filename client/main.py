import eel, os, time, threading

def finish():
    time.sleep(5)
    os.system("taskkill /im node.exe /F")

compile = threading.Thread(target=os.system, args=("npm run dev", ))
compile.start()
finish()
compile.join()

eel.init("public")

@eel.expose
def send():
    pass

def close_callback(route, websockets):
    if not websockets:
        exit()

eel.start("index.html", mode='electron', close_callback=close_callback)



