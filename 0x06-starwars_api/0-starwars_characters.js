#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a Movie ID');
  process.exit(1);
}

// URL for the Star Wars API to get the movie details
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie data');
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // For each character URL, make a request to get the character name
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to retrieve character data');
        return;
      }

      // Parse the response body as JSON
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

