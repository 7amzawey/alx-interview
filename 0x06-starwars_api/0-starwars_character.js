#!/usr/bin/env node

const request = require('request');
const filmId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, async function (error, response, body) {
  if (error) console.log(error);
  const chars = JSON.parse(body).characters;
  for (const charLink of chars) {
    await new Promise((resolve, reject) => {
      request(charLink, (error, response, body) => {
        if (error) console.log(error);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
