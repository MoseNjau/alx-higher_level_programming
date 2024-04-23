#!/usr/bin/node
// Script that prints all characters of a Star Wars movie.
const request = require('request');
const process = require('process');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, response, body) =>
        console.log(err || JSON.parse(body).name)
      );
    }
  }
});
