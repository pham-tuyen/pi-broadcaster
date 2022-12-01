import eel, os, threading

def eel_gui():
    print("ok eel is running")
    eel.init('src')
    eel_kwargs = dict(
                mode='edge',
                host="localhost",
                port=9000,
            )
    eel.start({'port': 5173}, **eel_kwargs)

ssr = threading.Thread(target=os.system, args=('npm run dev', ))
gui = threading.Thread(target=eel_gui)
ssr.start()
gui.start()
ssr.join()
gui.join()