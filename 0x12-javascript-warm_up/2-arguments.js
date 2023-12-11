#!/usr/bin/node
const { argv } = require('node:process');
const le = argv.length - 2;
if (le === 0) {
  console.log('No argument');
} else if (le === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
