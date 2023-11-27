#!/usr/bin/node
// Create a function to converts numbers from base 10 into other bases
exports.converter = function (base) {
  return num => num.toString(base);
};
