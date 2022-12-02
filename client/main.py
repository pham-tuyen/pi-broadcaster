import eel, sys

@eel.expose
def quit():
    sys.exit()

eel.init('src')

eel.start('index.html', mode='electron')