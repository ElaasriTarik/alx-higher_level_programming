#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2]);

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}

function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return (a * factorial(a - 1));
}
