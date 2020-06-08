var fs = require('fs')
var express = require('express');
var exec = require('child_process').exec;
var app = express();

app.get('/start', function(req, res){
    let key = req.query.key
    if (key == fs.readFileSync(__dirname + "/key.txt", 'utf8')) {
        exec('sudo systemctl start PyFyPi.service', (err, stdout, stderr) => {
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
        console.log("Invalid authentication key")
        res.send("Invalid authentication key")
    }
})

app.get('/stop', function(req, res){
    let key = req.query.key
    if (key == fs.readFileSync(__dirname + "/key.txt", 'utf8')) {
        exec('sudo systemctl stop PyFyPi.service', (err, stdout, stderr) => {
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
        console.log("Invalid authentication key")
        res.send("Invalid authentication key")
    }
})

app.listen(3001, function() {
  console.log('Server listening on port 3001!');
});
