#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const process = require('process');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const data = body;
    fs.writeFile(filePath, data, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
