#!/usr/bin/node
const args = process.argv;
if (Number(args[2])) {
  const j = Math.floor(Number(args[2]));
  for (let i = 0; i < j; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
