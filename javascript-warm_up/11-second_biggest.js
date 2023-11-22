#!/usr/bin/node
const args = process.argv.slice(2).sort(function (a, b) { return a - b; }).reverse();
if (!args[1]) {
  console.log(0);
} else {
  console.log(args[1]);
}
