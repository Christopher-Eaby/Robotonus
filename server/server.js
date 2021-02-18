const http = required('http');
const {readFile, readFileSync} = require('fs');
const server = http.createServer(function(re, res) {

});

server.Listen(1235, function(){
     console.log('Listening on port 1235')
});
=======
var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
    fs.readFile('ControlPanel.html', function(err, data) {
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write(data);
      return res.end();
    });
  }).listen(8080);