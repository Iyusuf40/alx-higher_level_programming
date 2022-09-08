#!/usr/bin/node
const Parent = require('./5-square.js');
class Square extends Parent {
  charPrint (c) {
    let str = '';
    const chr = c || 'X';
    for (let x = 0; x < this.width; x++) {
      str += chr;
    }
    for (let y = 0; y < this.width; y++) {
      console.log(str);
    }
  }
}
module.exports = Square;
