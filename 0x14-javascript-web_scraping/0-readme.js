#!/usr/bin/node
// Script that reads and prints the content of a file.
const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', (err, data) => console.log(err || data));
