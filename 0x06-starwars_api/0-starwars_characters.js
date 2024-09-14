#!/usr/bin/node
// request api through mode
const request = require('request');

// Step 1: Promisify the request function
function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to load, status code: ${response.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
}

const movieID = process.argv[2];

if (!movieID) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

// Step 3: Async function to fetch movie details and character names in order
async function fetchMovieCharacters(movieID) {
  try {
    // Fetch the data
    const movieUrl = `https://swapi.dev/api/films/${movieID}/`;
    const movieData = await requestPromise(movieUrl);
    const movieJson = JSON.parse(movieData);
    const characters = movieJson.characters;
    for (const characterUrl of characters) {
      const characterData = await requestPromise (characterUrl);
      const characterJson = JSON.parse(characterData);
      console.log(characterJson.name);
    }
  } catch (error) {
    console.error("Error:", error.message);
  }
}
fetchMovieCharacters(movieID);
