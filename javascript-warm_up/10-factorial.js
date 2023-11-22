#!/usr/bin/node

function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const args = process.argv;
let int = parseInt(args[2]);
if (isNaN(int)) {
  int = 1;
}
const fact = factorial(int);
console.log(fact);
