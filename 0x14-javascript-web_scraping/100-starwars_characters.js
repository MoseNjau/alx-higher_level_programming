#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  process.exit(1);
}
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body).characters;
  data.map(characterUrl => (
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const ch = JSON.parse(body);
      console.log(ch.name);
    })
  ));
});
