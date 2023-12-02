#!/usr/bin/node
// This function toggles the header between class red and class green when the
// toggle header button is pressed

$('#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
