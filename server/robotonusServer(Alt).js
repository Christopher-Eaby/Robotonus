//var io = require('socket.io')(http) 
var http = require('http');
var fs = require('fs');
var events = require('events');
//var PythonShell = require('python-shell');
//var pyshell = PythonShell(motorMovement);

const express = require('express')
const app = express()
const {spawn} = require('child_process')
const python = spawn('python', ['script1.py','node.js','python']);
var pyMotionArr = ['left.py', 'right.py', 'forward.py', 'backward.py'];
lenArr=pyMotionArr.length
//for (i=0; i < lenArray; i++) {
   //if (pyMotionArray[i]==) {

//   }
//}
const childPython = spawn('python', ['']);

childPython.stdout.on('data', (data) => {
    console.log('stdout: ${data}');
});

childPython.stderr.on('data', (data) => {
  console.log('stderr: ${data}');
});

childPython.stdout.on('close', (data) => {
  console.log('child process exited with code ${data}');
});

app.post('/instructions', function(reg, pes){
     

});
app.listen(1738);

http.createServer(function (req, res) {
  fs.readFile('Robotonus_index.html', function(err, data) {
     res.writeHead(200, {'Content-Type': 'text/html'});
     res.write(data);
     return res.end();
  });
}).listen(4200);


   