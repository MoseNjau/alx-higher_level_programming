#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (const result of results) {
      for (const character of result.characters) {
        if (character.includes('18')) count++;
      }
    }
    console.log(count);
  }
});
