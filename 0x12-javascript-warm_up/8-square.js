#!/usr/bin/node
const x = parseInt(process.argv[2]);
let str = '';
if (x) {
  for (let y = 0; y < x; y++) {
    str += 'x';
  }
  for (let y = 0; y < x; y++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
