#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

console.log(`Requesting URL: ${url}`);

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  let film;
  try {
    film = JSON.parse(body);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    return;
  }

  const characters = film.characters;
  if (!characters) {
    console.error('No characters found in the film data.');
    return;
  }

  const printChars = (i) => {
    if (i === characters.length) return;

    request(characters[i], (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }
      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', charResponse.statusCode);
        return;
      }

      let character;
      try {
        character = JSON.parse(charBody);
      } catch (charParseError) {
        console.error('Error parsing JSON:', charParseError);
        return;
      }

      console.log(character.name);
      printChars(i + 1);
    });
  };

  printChars(0);
});
