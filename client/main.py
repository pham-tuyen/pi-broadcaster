import eel, paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.2.100", username="root", password="123456")

eel.init("public")

@eel.expose
def send():
    pass

eel.start("index.html", mode='electron')



