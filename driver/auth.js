var querystring = require('querystring');
var request = require('request')
var rp = require('request-promise')
var http = require('http');

exports.requestToken = function(code, secret) {

  console.log("requesting a token")
  //console.log("code: " + code)
  //console.log("secret: " + secret)


  return rp.post('https://accounts.spotify.com/api/token', {
    headers: {'content-type' : 'application/x-www-form-urlencoded'},
    form: {
      'grant_type': 'authorization_code',
      'code': code,
      'redirect_uri': 'http://localhost:3000/authenticated',
      'client_id': '31f47db1c9b043b78f5ca5fbc53ac1d5',
      'client_secret' : secret
    }
  })
}

exports.requestRefresh = function(refreshToken, secret) {
  console.log("requesting refresh token")

  return rp.post('https://accounts.spotify.com/api/token', {
    headers: {'content-type' : 'application/x-www-form-urlencoded'},
    form: {
      'grant_type': 'refresh_token',
      'refresh_token' : refreshToken,
      'client_id': '31f47db1c9b043b78f5ca5fbc53ac1d5',
      'client_secret' : secret
    }
  })


// // Build the post string from an object
//   var post_data = querystring.stringify({
//     'grant_type' : 'refresh_token',
//     'refresh token' : refreshToken,
//     'client_id' : '31f47db1c9b043b78f5ca5fbc53ac1d5',
//     'client_secret' : secret
//   });

//   // An object of options to indicate where to post to
//   var post_options = {
//     host: 'accounts.spotify.com',
//     port: '80',
//     path: '/api/token',
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/x-www-form-urlencoded',
//       'Content-Length': Buffer.byteLength(post_data)
//     }
//   };

//   // Set up the request
//   var post_req = http.request(post_options, function(res) {
//     res.setEncoding('utf8');
//     res.on('data', function (chunk) {
//         console.log('Response: ' + chunk);
//     });
//   });

//   post_req.on('error', (e) => {
//     //TODO: get token from here
//     console.error(`problem with request: ${e.message}`);
//   });
//   res.on('end', () => {
//     console.log('No more data in response.');
//   });
}