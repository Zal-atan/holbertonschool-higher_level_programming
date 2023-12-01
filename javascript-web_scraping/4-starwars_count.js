#!/usr/bin/node
// This program displays the displays number of star wars films in which the character “Wedge Antilles” is present.
// website given as {argument 1]}

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  let counter = 0;
  const fullJson = (JSON.parse(body).results);

  // Iterate over list of Jsons
  for (const movie in fullJson) {
    const allChars = fullJson[movie].characters;
    for (const char in allChars) {
      if (char === 18) {
        counter++;
      }
    }
  }
  console.log(counter);
});
