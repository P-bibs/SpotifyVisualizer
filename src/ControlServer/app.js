var fs = require('fs')
var express = require('express');
var exec = require('child_process').exec;
var app = express();

app.get('/start', function(req, res){
    let key = req.query.key
    let execError;
    if (key == fs.readFileSync(__dirname + "/key.txt", 'utf8')) {
        exec('sudo systemctl start pyfypi.service', (err, stdout, stderr) => {
            if (err) {
                console.log("Error")
                console.log(err)
                return;
            }
            // the *entire* stdout and stderr (buffered)
            console.log(`stdout: ${stdout}`);
            console.log(`stderr: ${stderr}`);
        });
    }
    else {
        res.send("Invalid authentication key")
    }
    if (execError == ""){
        res.send(`Error:\n ${execError}`)
    }
    else {
        res.send("Success")
    }
})

app.get('/stop', function(req, res){
    let key = req.query.key
    let execError = "";
    if (key == fs.readFileSync(__dirname + "/key.txt", 'utf8')) {
        exec('sudo systemctl stop pyfypi.service', (err, stdout, stderr) => {
            if (err) {
                console.log("Error")
                console.log(err)
                return;
            }
            // the *entire* stdout and stderr (buffered)
            console.log(`stdout: ${stdout}`);
            console.log(`stderr: ${stderr}`);
        });
    }
    else {
        res.send("Invalid authentication key")
    }
    if (execError == ""){
        res.send(`Error:\n ${execError}`)
    }
    else {
        res.send("Success")
    }
})

app.listen(3001, function() {
  console.log('Server listening on port 3001!');
});
