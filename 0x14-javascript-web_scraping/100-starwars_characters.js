#!/usr/bin/node
/* gets a movie by id and prints the names of actors in it */

const request = require('request');
const fs = require('fs');

const id = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + id;
const peopleUrl = 'https://swapi-api.hbtn.io/api/people';
let people = {};
const file = 'save.json';

request(filmUrl, (err, resp, body) => {
  if (!err) {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (!err) {
        request(peopleUrl, (error, resp, body) => {
          if (!error) {
            fs.readFile(file, 'utf-8', (err, data) => {
              if (err) {
                console.log(err);
              }
              const film = JSON.parse(data);
              people = JSON.parse(body);
              printNames(film.characters, people.results);
            });
          }
        });
      }
    });
  }
});

function printNames (filmChars, peopleList) {
  const peopleByUrl = {};
  for (const person of peopleList) {
    peopleByUrl[person.url] = person.name;
  }
  for (const character of filmChars) {
    if (peopleByUrl[character]) {
      console.log(peopleByUrl[character]);
    }
  }
}
