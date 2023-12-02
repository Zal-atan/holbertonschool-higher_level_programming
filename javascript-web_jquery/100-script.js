#!/usr/bin/node
// This program updates the color of <header> to red

document.addEventListener("DOMContentLoaded", function () {
    const headerFix = document.querySelector('header');
    headerFix.style.color = '#ff0000';
})
