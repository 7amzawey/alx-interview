#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, async function (error, response, body) {
  if (error) console.error(error);
  const chars = JSON.parse(body).characters;
  for (const char of chars) {
    await new Promise(function (resolve, reject) {
      request(char, (error, response, body) => {
        if (error) console.error(error);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
