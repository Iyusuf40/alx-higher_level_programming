#!/usr/bin/node
const value = parseInt(process.argv[2]);
function factorial (value) {
  if (!value) {
    return 1;
  }
  return value * factorial(value - 1);
}
console.log(factorial(value));
