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
//include the countdown file so that we can use the countdown function
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

    mainWindow.on('closed', _ => {
        mainWindow = null
    })
})

ipc.on('countdown-start', _ => {
    //send the count back to the countdown function
    countdown(count => {
        //emits a new event called coundown and we're sending count as the argument
        mainWindow.webContents.send('countdown', count)
    })
})
```

countdown.html. Notice that we're able to use the node `require()` statement. That's because in our main process, we set nodeintegration to true.

```html
<html>
    <head>

    </head>
    <body>
        <button id="start">Start</button>
        <div id="count"></div>
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

//this is a handler for when the countdown event is received
ipc.on('countdown', (evt, count) => {
    // display the count in an element called count
    document.getElementById('count').innerHTML = count
})
```

You'll notice that for this particular project, we're using a js file to export to the main file call `countdown.js`

```js
module.exports = function countdown(tick){
    //tick is acting as a callback function
    console.log('begin countdown')
    let count = 10

    let timer = setInterval(_ => {
        // sending the decrement of count to the callback function
        tick(count--)
        if(count === 0){
            clearInterval(timer)
        }
    }, 1000)
}
```

# Application Menu

Use the following sample code to create an application menu


```js
const electron = require('electron')
const app = electron.app 
const BrowserWindow = electron.BrowserWindow 
const Menu = electron.Menu 

app.on('ready', _ => {
    new BrowserWindow()
    const template = [
        {
            label: electron.app.getName(),
            submenu: [{
                label: `About ${name}`,
                click: _ => {
                    console.log('clicked')
                },
                role: 'about'
            }              
            ]
        }
    ]
    const menu = Menu.buildFromTemplate(template)
    Menu.setApplicationMenu(menu)
})
```

# System Tray

A cool feature is that we can add in a tray icon. We need to do the following two items.

1. Where we're defining our electron constants at the top, we can add `const Tray = electron.Tray`

Our constants are now getting a little crowded so we'll take advantage of array destructuring with 

```js
const {app,Menu,Tray} = electron
```

2. Inside of our app.ready, we'll also use the following

```js
const tray = New Tray(path.join('src', 'trayIcon.png'))
```
