var querystring = require('querystring');
var http = require('http');

function readCode(path) {
    //TODO: Read code from memory
}

function requestToken(code) {
  // Build the post string from an object
  var post_data = querystring.stringify({
    'grant_type' : 'authorization_code',
    'code': code,
    'redirect_uri': 'http://localhost/authenticated',
    'client_id' : '', //TODO
    'client_secret' : '' //TODO
  });

  // An object of options to indicate where to post to
  var post_options = {
    host: 'accounts.spotify.com',
    port: '80',
    path: '/api/token',
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': Buffer.byteLength(post_data)
    }
  };

  // Set up the request
  var post_req = http.request(post_options, function(res) {
    res.setEncoding('utf8');
    res.on('data', function (chunk) {
        console.log('Response: ' + chunk);
    });
  });

  post_req.on('error', (e) => {
    //TODO: get token  and refresh token from here
    console.error(`problem with request: ${e.message}`);
  });
  res.on('end', () => {
    console.log('No more data in response.');
  });
}

function refreshToken(refreshToken) {
// Build the post string from an object
  var post_data = querystring.stringify({
    'grant_type' : 'refresh_token',
    'refresh token' : refreshToken,
    'client_id' : '', //TODO
    'client_secret' : '' //TODO
  });

  // An object of options to indicate where to post to
  var post_options = {
    host: 'accounts.spotify.com',
    port: '80',
    path: '/api/token',
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': Buffer.byteLength(post_data)
    }
  };

  // Set up the request
  var post_req = http.request(post_options, function(res) {
    res.setEncoding('utf8');
    res.on('data', function (chunk) {
        console.log('Response: ' + chunk);
    });
  });

  post_req.on('error', (e) => {
    //TODO: get token from here
    console.error(`problem with request: ${e.message}`);
  });
  res.on('end', () => {
    console.log('No more data in response.');
  });
}