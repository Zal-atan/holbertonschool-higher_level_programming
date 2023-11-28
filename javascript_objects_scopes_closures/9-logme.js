#!/usr/bin/node
// Prints number of logs: item
let numLogs = 0;
exports.logMe = function (item) {
  const message = numLogs + ': ' + item;
  console.log(message);
  numLogs += 1;
};
