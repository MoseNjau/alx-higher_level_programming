#!/usr/bin/node

const occurNum = parseInt(process.argv[2]);
const str = 'C is fun';
if (occurNum) {
  for (let index = 0; index < occurNum; index++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
