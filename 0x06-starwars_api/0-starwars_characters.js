#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const filmData = JSON.parse(body);
  const chars = filmData.characters;
  chars.forEach(charLink => {
    request(charLink, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  });
});
