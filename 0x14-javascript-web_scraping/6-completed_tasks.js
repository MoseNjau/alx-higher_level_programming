#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const results = JSON.parse(body);
    const completed = {};
    for (const result of results) {
      if (result.completed) {
        if (completed[result.userId]) completed[result.userId]++;
        else completed[result.userId] = 1;
      }
    }
    console.log(completed);
  }
});
