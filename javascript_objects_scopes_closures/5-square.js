#!/usr/bin/node
// Loads Rectangle
const Rectangle = require('./4-rectangle.js');

// Creates class Square by Extending Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
