#!/usr/bin/node

const fs = require('node:fs');
const request = require('request');
const filename = process.argv[3];
const url = process.argv[2];

if (!url) console.log(undefined);
else {
  request(url, (err, response) => {
    if (err) console.log(err);
    else {
      const data = response.body;
      fs.writeFile(filename, data, err => {
        if (err) console.log(err);
      });
    }
  });
}
