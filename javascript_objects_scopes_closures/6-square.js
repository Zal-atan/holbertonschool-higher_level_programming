#!/usr/bin/node
// Loads Rectangle
const Rectangle = require('./4-rectangle.js');

// Creates class Square by Extending Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // Print a square using char c, or "X" if undefined
  charPrint (c = 'X') {
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
