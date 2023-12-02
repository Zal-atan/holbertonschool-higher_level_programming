#!/usr/bin/node
// This function adds element <li>Item</li> each time the DIV#add_item tag is pressed

$('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>')
})
