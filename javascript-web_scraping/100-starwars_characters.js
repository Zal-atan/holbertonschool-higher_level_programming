#!/usr/bin/node
// This program displays all of the characters from Star wars movie number {argument 1]}

const request = require('request');
const website = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(website, function (err, response, body) {
  if (err) throw err;
  // Get each characters website
  const characters = JSON.parse(body).characters;
  // For Each website
  characters.forEach(function (char) {
    request(char, function (err, response, body) {
      if (err) throw err;
      // Print character name
      console.log(JSON.parse(body).name);
    });
  });
});
