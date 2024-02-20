#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) console.log(undefined);
else {
  request.head(url, (err, response) => {
    if (err) console.log(err);
    else {
      console.log('code:', response.statusCode);
    }
  });
}
