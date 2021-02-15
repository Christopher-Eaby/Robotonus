const http = required('http');
const {readFile, readFileSync} = require('fs');
const server = http.createServer(function(re, res) {

});

server.Listen(1235, function(){
     console.log('Listening on port 1235')
});