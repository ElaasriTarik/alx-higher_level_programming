#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);

add(a, b);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
