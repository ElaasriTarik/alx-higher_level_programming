#!/usr/bin/node
const args = process.argv;

if (args.length === 2) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  let big = 0;
  let sec = 0;

  for (let x = 2; x < args.length; x++) {
    if (parseInt(args[x]) > big) {
      sec = big;
      big = parseInt(args[x]);
    }
  }
  console.log(sec);
}
