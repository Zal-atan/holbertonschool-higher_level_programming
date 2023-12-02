#!/usr/bin/node
// This function fetches the word hello translated into another language
// and places it in the tag DIV#hello

const website = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$('document').ready(function () {
  // Get the whole website JSON data
  $.get(website, function (data) {
    // Change text inside #hello
    $('#hello').text(data.hello);
  });
});
