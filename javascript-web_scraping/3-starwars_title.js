#!/usr/bin/node
// This program displays the displays a star wars name from a number input {argument 1]}

const request = require('request');
const website = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];

request(website, function (err, response, body) {
  if (err) throw err;
  console.log(JSON.parse(body));
});
