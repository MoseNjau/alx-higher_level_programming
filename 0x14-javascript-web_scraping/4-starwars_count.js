#!/usr/bin/node

const request = require('request');

const url = process.argv[2] ?? '';
const id = '18';
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body).results;
  const films = [];
  data.map(film => films.push(...film.characters));
  const filtered = films.filter(el => el.endsWith(id + '/'));
  console.log(filtered.length);
});
