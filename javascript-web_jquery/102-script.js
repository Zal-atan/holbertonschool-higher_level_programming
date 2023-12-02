#!/usr/bin/node
// This function fetches the word hello translated into another language
// and places it in the tag DIV#hello

const website = 'https://hellosalut.stefanbohacek.dev/?lang=';

$('document').ready(function () {
    // When button is clicked
  $('#btn_translate').click(function () {
    console.log(website)
    // Get the whole website JSON data
    $.get(website + $("#language_code").val(), function (data) {
      // Change text inside #hello
      $('#hello').text(data.hello);
    });
  })
});
