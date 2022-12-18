import eel, sys, os, threading


def gui():
    eel.init("public")

    #expose Python API

    def close_callback(route, websockets):
        if not websockets:
            sys.exit()

    eel.start('index.html', mode='electron', close_callback=close_callback)

frontend = threading.Thread(target=gui)
backend = threading.Thread(target=os.system, args=("npm run dev",))

backend.start()
frontend.start()

backend.join()
frontend.join()
