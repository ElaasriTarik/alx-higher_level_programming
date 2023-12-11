#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2]);
if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < value; x++) {
    let numX = '';
    for (let y = 0; y < value; y++) {
      numX += 'X';
    }
    console.log(numX);
  }
}
