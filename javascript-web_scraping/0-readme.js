#!/usr/bin/node
// This program Reads from file which is the first argument given

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
