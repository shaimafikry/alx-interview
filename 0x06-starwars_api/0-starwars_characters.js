#!/usr/bin/node
// request api through mode
const request = require('request');

function getCharacter(id){
  // function to get the data
  // url
  url = 'https://swapi-api.alx-tools.com/api/'
  film = url + `films/${id}`;
  request.get(film, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movie = JSON.parse(body);
      // console.log(movie)
      movie.characters.forEach((characterUrl) => {
        request.get(characterUrl, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}




const id = process.argv[2]
// console.log(id)

if (id){
  getCharacter(id);
}
else{
  console.log('There must be an id provided first')
}
