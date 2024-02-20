#!/usr/bin/node

const request = require('request');
const id = 18;
const url = process.argv[2];
let number = 0;
if (!url) console.log(undefined);
else {
  request(url, (err, response) => {
    if (err) console.log(err);
    else {
      const data = JSON.parse(response.body).results;
      for (let x = 0; x < data.length; x++) {
        data[x].characters.forEach(char => {
          if (char.includes(id)) { number++; }
        });
      }
      console.log(number);
    }
  });
}
