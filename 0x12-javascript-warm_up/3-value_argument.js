#!/usr/bin/node
const args = process.argv;
let x = 0;
while (args[x]) {
  if (x === 2) {
    console.log(args[x]);
  }
  x++;
}
if (x === 2) {
  console.log('No arguments');
}
