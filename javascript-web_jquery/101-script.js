#!/usr/bin/node
// This function adds to, removes from, and clears a list based on button pressed

// This must be added for multiple functions in one file
$('document').ready(function () {
  // Adds new items
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  // Removes last item from list
  $('#remove_item').click(function () {
    $("UL.my_list li:last").remove();
  })
  // Clear the list
  $('#clear_list').click(function () {
    $("UL.my_list").empty();
  })
})
