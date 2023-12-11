#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2]);
if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  let x = 0;
  for (; x < value; x++) {
    console.log('C is fun');
  }
}
