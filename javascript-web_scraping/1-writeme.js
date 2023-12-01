#!/usr/bin/node
// This program writes a string given as argument 2 to a file argument 1

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) throw err;
});
