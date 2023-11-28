#!/usr/bin/node
const list1 = require('./100-data.js').list;

console.log(list1);
const list2 = list1.map((num, idx) => num * idx);
console.log(list2);
