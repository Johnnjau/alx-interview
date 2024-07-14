#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  printChars(characters, 0);
});
const printChars = (characters, i) => {
  if (i === characters.length) return;
  request(characters[i], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printChars(characters, i + 1);
  });
};
