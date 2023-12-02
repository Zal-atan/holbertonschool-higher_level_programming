#!/usr/bin/node
// This program displays all of the characters from Star wars movie number {argument 1]}

const request = require('request');
const website = 'https://swapi-api.hbtn.io/api/films/';

request(website, function (err, response, body) {
  if (err) throw err;
  const movies = JSON.parse(body).results;
  movies.forEach(function (film) {
    if (film.episode_id == process.argv[2]) {
      // Get each characters website
      const characters = film.characters;
      // console.log(characters)
      // // For Each website
      for (char in characters) {
        request(characters[char], function (err, response, body) {
          if (err) throw err;
          // Print character name
          console.log(JSON.parse(body).name);
        });
      }
    };
  });
});
