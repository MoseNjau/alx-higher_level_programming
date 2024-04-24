#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const results = {};
  data.map(user => {
    if (user.completed) {
      if (results[user.userId]) {
        results[user.userId] += 1;
      } else {
        results[user.userId] = 1;
      }
    }
  });

  console.log(results);
});
