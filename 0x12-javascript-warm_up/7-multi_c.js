#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x) {
  for (let y = 0; y < x; y++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
