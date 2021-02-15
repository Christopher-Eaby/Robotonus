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