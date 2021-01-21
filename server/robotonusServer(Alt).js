var io = require('socket.io')(http) 
var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
  fs.readFile('Robotonus_index.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });

  fs.readFile('Movement.py', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/python'});
    res.write(data);
    return res.end();
  });
}).listen(8080);

