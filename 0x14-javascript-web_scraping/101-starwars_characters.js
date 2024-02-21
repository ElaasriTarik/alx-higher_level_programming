#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

if (!url) console.log(undefined);
else {
	request(url, (err, response) => {
		if (err) console.log(err);
		else {
			const data = JSON.parse(response.body);
			const chars = data.characters.slice().sort();
			chars.forEach(characterURL => {
				request(characterURL, (err, res) => {
					if (err) console.log(err);
					else {
						const charInfo = JSON.parse(res.body);
						console.log(charInfo.name);
					}
				});
			});
		}
	});
}
