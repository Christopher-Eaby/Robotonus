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

