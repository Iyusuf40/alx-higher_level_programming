#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let x = 0; x < this.width; x++) {
      str += 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(str);
    }
  }

  rotate () {
    const store = this.height;
    this.height = this.width;
    this.width = store;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
