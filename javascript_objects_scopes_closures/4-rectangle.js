#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Exchanges width and Height of rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Double the width and height of rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
