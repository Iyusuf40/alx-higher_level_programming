#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x) {
  for (let y = 0; y < x; y++) {
    if (y) {
      process.stdout.write('\n');
    }
    for (let z = 0; z < x; z++) {
      process.stdout.write('x');
    }
  }
  process.stdout.write('\n');
} else {
  console.log('Missing size');
}
