
var express = require('express');
var app = express();

// app.get('/', function(req, res) {
//   res.send('Hello World!');
// });

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});


app.get('/authenticated', function(req, res) {
    let code = req.query.code
    writeCode(code)
    res.send("You may now close this page")
});

app.listen(3000, function() {
  console.log('Example app listening on port 3000!');
});

//Change this function when switching from dev to build
function writeCode(code) {
    fs.writeFile("/tmp/test", "Hey there!", function(err) {
        if(err) {
            return console.log(err);
        }

        console.log("The file was saved!");
    });
}