#!/usr/bin/node
// request api through mode
const request = require('request-promise');

// Step 1: Get the movie ID from the command line arguments
const movieID = process.argv[2];

if (!movieID) {
  console.error("Please provide a movie ID as the first argument.");
  process.exit(1);
}

// Step 2: Function to fetch movie details
async function fetchMovieCharacters(movieID) {
  try {
    // Fetch the movie data
    const url = `https://swapi.dev/api/films/${movieID}/`;
    const movieData = await request({ uri: url, json: true });

    // Step 3: Extract the character URLs
    const characters = movieData.characters;

    // Step 4: Fetch and print character names in order
    for (const characterUrl of characters) {
      const characterData = await request({ uri: characterUrl, json: true });
      console.log(characterData.name);
    }
  } catch (error) {
    console.error("Error fetching data:", error.message);
  }
}

// Step 5: Call the function to fetch movie characters
fetchMovieCharacters(movieID);