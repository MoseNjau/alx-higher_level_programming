#!/usr/bin/node
arg = process.argv[2];
argNum = parseInt(arg);

if (!isNaN(argNum)) {
    for (i = 0; i < argNum; i++) {
        console.log("C is fun")
    }
} else {
    console.log("Missing number of occurrences")
}