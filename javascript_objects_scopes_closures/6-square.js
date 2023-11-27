#!/usr/bin/node
// Loads Rectangle
const Sq = require('./5-square.js');

// Extends class Square
class Square extends Sq {
  // Print a square using char c, or "X" if undefined
  charPrint (c = 'X') {
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
