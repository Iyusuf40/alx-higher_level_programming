#!/usr/bin/node
function add (a, b) {
  const res = parseInt(a) + parseInt(b);
  console.log(res);
}

add(process.argv[2], process.argv[3]);
