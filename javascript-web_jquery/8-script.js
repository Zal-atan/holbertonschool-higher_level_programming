#!/usr/bin/node
// This function fetches the names of each starwars movie and list them in the
// UL#list_movies tag

const website = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Get the whole website JSON data
$.get(website, function (data) {
  // For each movie in data.results
  $.each(data.results, function (i, movie) {
    // console.log(movie.title)
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
