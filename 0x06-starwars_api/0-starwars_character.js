#!/usr/bin/env node

const request = require('request');
const filmId = process.argv[2];

if (!filmId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, async function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  try {
    const chars = JSON.parse(body).characters;
    for (const charLink of chars) {
      await new Promise((resolve, reject) => {
        request(charLink, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
            reject(error);
            return;
          }
          try {
            console.log(JSON.parse(body).name);
            resolve();
          } catch (parseError) {
            console.error('Error parsing character data:', parseError);
            reject(parseError);
          }
        });
      });
    }
  } catch (parseError) {
    console.error('Error parsing film data:', parseError);
  }
});
