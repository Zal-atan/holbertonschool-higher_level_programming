#!/usr/bin/node
const args = process.argv;
if (!args[2]) {
  console.log('Not a number');
} else {
  if ((Number(args[2]))) {
    console.log(`My number: ${Math.floor(Number(args[2]))}`);
  } else {
    console.log('Not a number');
  }
}
