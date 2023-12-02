#!/usr/bin/node
// This function fetches the word hello translated into another language
// and places it in the tag DIV#hello

const website = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Get the whole website JSON data
$.get(website, function (data) {
  // For each movie in data.results
  $('#hello').text(data.hello);
});
