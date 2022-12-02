const {app, BrowserWindow} = require('electron')

const createWindow = () => {
    const window = new BrowserWindow()
    window.loadFile("./src/index.html")
    window.setTitle('Bảng điều khiển')
    window.maximize()
}

app.whenReady().then(() => {
    createWindow()
    app.on('activate', () => {
        if(BrowserWindow.getAllWindows90.length === 0) createWindow()
    })
})

app.on('window-all-closed', () => {
    if(process.platform !== 'darwin') app.quit()
})