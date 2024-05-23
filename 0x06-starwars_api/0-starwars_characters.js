#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

request.get(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((characterUrl, index) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);

      if (index === characters.length - 1) {
        process.exit(0);
      }
    });
  });
});
