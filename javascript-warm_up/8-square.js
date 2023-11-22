#!/usr/bin/node
const args = process.argv;
const int = parseInt(args[2]);
if (int) {
  for (let i = 0; i < int; i++) {
    console.log('X'.repeat(int));
  }
} else {
  console.log('Missing size');
}
