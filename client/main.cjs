const {app, BrowserWindow} = require('electron')
const path = require('path')
const waitPort = require('wait-port');
const { exec } = require('child_process');

const params = {
    host: 'localhost',
    port: 4173,
};

const createWindow = () => {
    var splash = new BrowserWindow({ 
        width: 500, 
        height: 300, 
        transparent: true, 
        frame: false, 
        alwaysOnTop: true 
    });
    
    splash.loadURL(path.join(__dirname, "/splash/splash.html"));
    splash.center();
    setTimeout(function () {
        splash.close();

        const window = new BrowserWindow({
            autoHideMenuBar: true,
            show: false
        })

        waitPort(params)
            .then(({open}) => {
                if(open) window.loadURL("http://localhost:4173")
            })
            .catch((err) => {
                console.err(`An unknown error occured while waiting for the port: ${err}`);
            });
        
        window.center();
        window.show();
        window.setTitle('Bảng điều khiển')
        window.setIcon(path.join(__dirname, '/static/pi.png'))
        window.maximize()
    }, 5000);
}

app.whenReady().then(() => {
    createWindow()
    app.on('activate', () => {
        if(BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})

app.on('window-all-closed', () => {
    exec('npx kill-port 8000', (err, stdout, stderr) => {
        if (err) {
          return;
        }
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
      });
      exec('npx kill-port 4173', (err, stdout, stderr) => {
        if (err) {
          return;
        }
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
      });
      exec('taskkill /im python.exe /F || taskkill /im node.exe /F', (err, stdout, stderr) => {
        if (err) {
          return;
        }
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
      });
    if(process.platform !== 'darwin') app.quit()
})