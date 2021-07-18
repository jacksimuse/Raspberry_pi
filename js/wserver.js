var http = require('http');
var fs = require('fs');
var app = http.createServer(function (req, res) {
    var url = req.url;
    if(url == '/')
    {
        url = '/index.html';
    }
    res.writeHead(200);
    res.end(fs.readFileSync(__dirname + url))    // dirname : js가 실행되는 파일 위치
}).listen(8080, '127.0.0.1')
console.log('WebServer is running at http://127.0.0.1:8080')