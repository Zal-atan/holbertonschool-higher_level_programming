#!/usr/bin/node
const args = process.argv;
const int1 = parseInt(args[2]);
const int2 = parseInt(args[3]);
if (isNaN(int2)) {
  console.log('NaN');
} else {
  console.log(int1 + int2);
}
