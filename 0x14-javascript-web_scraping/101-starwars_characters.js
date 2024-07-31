#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

if (!id) {
  console.error('Please provide a film ID as an argument.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch film data. Status code: ${response.statusCode}`);
  } else {
    try {
      const content = JSON.parse(body);
      const characters = content.characters;

      for (const character of characters) {
        request.get(character, (charError, charResponse, charBody) => {
          if (charError) {
            console.error

