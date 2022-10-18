#!/usr/bin/node
/* script reads a file and prints its content */

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, 'utf-8', (err, d) => {
  if (err) {
    console.log(err);
  }
}
);
