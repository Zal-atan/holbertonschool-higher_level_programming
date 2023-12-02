#!/usr/bin/node
// This function updated <header> element to text "New Header!!!" when the
// DIV#update_header tag is clicked on

$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
