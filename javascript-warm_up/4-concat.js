#!/usr/bin/node
const args = process.argv;
let first = 'undefined';
let second = 'undefined';
if (args[3]) {
  first = args[2];
  second = args[3];
} else if (args[2]) {
  first = args[2];
}
console.log(`${first} is ${second}`);
