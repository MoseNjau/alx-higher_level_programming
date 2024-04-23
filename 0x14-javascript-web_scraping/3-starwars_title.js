#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const process = require('process');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, (err, response, body) =>
  console.log(err || JSON.parse(body).title)
);
