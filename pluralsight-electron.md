1. Install with `npm install electron`
2. Create an src/main.js file
3. Edit package.json as the following

```js
{
  ...
  "main": "src/main.js",
  "scripts": {
    "start": "electron ."
  },
  ...
}
```
*Notice that we've shortened the script to show the main parts.*

# Processes

Electron works on a main process and a renderer process. the main process is like the server receiving the data from the client, the renderer process. The renderer will send data through an IPC (inter process connect)

# Create Project

The folowing is taken from a sample course on pluralsight.

Create three files: main.js, renderer.js, and countdown.js

main.js. This is our main file that acts as the main process and will receive events from the renderer processes. Notice that we're referencing an html file so let's create that next.

```js
const electron = require('electron')
const countdown = require('./countdown.js')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const ipc = electron.ipcMain

//instantiate browser window
let mainWindow

app.on('ready', _ => {
    mainWindow = new BrowserWindow({
        height: 400,
        width: 400,
        webPreferences: {
            nodeIntegration: true
        }
    })

    mainWindow.loadURL(`file://${__dirname}/countdown.html`)

    countdown()

    mainWindow.on('closed', _ => {
        mainWindow = null
    })
})

ipc.on('countdown-start', _ => {
    console.log('caught')
})
```

countdown.html. Notice that we're able to use the node `require()` statement. That's because in our main process, we set nodeintegration to true.

```html
<html>
    <head>

    </head>
    <body>
        <button id="start">Start</button>
        <script>require('./renderer.js')</script>
    </body>
</html>
```

renderer.js

```js
const electron = require('electron')

const ipc = electron.ipcRenderer

document.getElementById('start').addEventListener('click', _ => {
    //sending the countdown-start event to the main process
    ipc.send('countdown-start')
})
```
