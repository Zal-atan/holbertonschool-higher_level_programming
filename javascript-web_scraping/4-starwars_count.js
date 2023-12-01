#!/usr/bin/node
// This program displays the displays number of star wars films in which the character “Wedge Antilles” is present.
// website given as {argument 1]}

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  console.log(JSON.parse(body).results);
});
