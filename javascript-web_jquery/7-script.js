#!/usr/bin/node
// This function fetches the character name at the given URL

const website = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(website, function (character) {
  $('#character').text(character.name);
});
