#!/usr/bin/node
// Copies the contents of website (argument 1) into a file named (argument 2)

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) throw err;
  });
});
