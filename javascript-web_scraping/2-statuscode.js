#!/usr/bin/node
// This program displays the status code of a get request from website {argument 1}

const request = require('request');

request(process.argv[2], function (err, response) {
  if (err) throw err;
  console.log('code:' + response.statusCode);
});
