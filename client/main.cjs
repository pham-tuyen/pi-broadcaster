const {app, BrowserWindow} = require('electron')
const path = require('path')

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
        window.loadURL("http://localhost:4173")
        
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
    if(process.platform !== 'darwin') app.quit()
})