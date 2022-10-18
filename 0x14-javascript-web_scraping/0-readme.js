#!/usr/bin/node
/* script reads a file and prints its content */

const fs = require('node:fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', (err, d) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(d);
}
);
