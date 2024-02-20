#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const users = {};
if (!url) console.log(undefined);
else {
	request(url, (err, response) => {
		if (err) console.log(err);
		else {
			const data = JSON.parse(response.body);
			for (let x = 0; x < data.length; x++) {
				const user = data[x].userId;
				if (Object.prototype.hasOwnProperty.call(users, `${user}`)) {
					if (data[x].completed === true) {
						users[`${user}`] += 1;
						if (users[`${user}`] === 0) delete users[`${user}`];
					}
				} else {
					users[`${user}`] = 0;
				}

			}
			console.log(users);
		}
	});
}
