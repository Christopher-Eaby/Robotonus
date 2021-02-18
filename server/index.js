const Html5WebSocket = require('html5-websocket');
const ReconnectingWebSocket = require('reconnecting-websocket');

let ws_host = 'localhost';
let ws_port= '4000';
const options = { WebSocket: Html5WebSocket };
const rws = new ReconnectingWebSocket('ws://' + ws_host + ':' + ws_port + '/ws', undefined, options);
rws.timeout=1000;

rws.addEventListener('open', () => {
    console.log('[Client] Connected');
    rws.send('Ping');
});

rws.addEventListener('close', () => {
    console.log('[Client] Disconnected');
    rws.send('Ping');
});

rws.onerror = (err) => {
    if (err.code == 'EHOSTDOWN') {
         console.log('[Client] Error:server down.');
    }
};
=======
const express = require('express');
const app = express();
var http =require('http');
const spawn = require('child_process').spawn;
const childPython1 = spawn('python', ['forward.py']);
const childPython2 = spawn('python', ['back.py']);
const childPython3 = spawn('python', ['left.py']);
const childPython4 = spawn('python', ['right.py']);
const server = express().listen(1738);

app.listen(3000, () => console.log('port 3000'));
app.use(express.static('public'));
app.use(express.json({limit: 'lmb'}));

message="";

app.post('/button', (request, response) => {
     console.log(request.body);
     message=request.body;
});

switch (message) {
    case (message=="forward"):
        childPython1.stdout.on('data', data => {
            console.log(data.toString());
        });
        break;
    case (message=="back"):
        childPython2.stdout.on('data', data => {
            console.log(data.toString());
        });
        break;
    case (message=="left"):
        childPython3.stdout.on('data', data => {
            console.log(data.toString());
        });
        break;
    case (message=="right"):
        childPython4.stdout.on('data', data => {
            console.log(data.toString());
        });
        break;
}