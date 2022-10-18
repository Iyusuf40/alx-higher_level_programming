#!/usr/bin/node
/* gets a movie by id and prints the names of actors in it */

const util = require('util');
const request = util.promisify(require('request'));

const id = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + id;
const peopleUrl = 'https://swapi-api.hbtn.io/api/people/?page=';
const peopleId = {};

async function main () {
  const filmChars = await request(filmUrl)
    .then(e => {
      return (JSON.parse(e.body).characters);
    })
    .catch(e => {
      console.log(e);
    });
  let index = 1;
  for (index = 1; index > 0; index++) {
    const id = index.toString();
    const url = peopleUrl + id;
    await request(url)
      .then(res => {
        const results = JSON.parse(res.body).results;
        if (!results) {
          index = -2;
        } else {
          for (const item of results) {
            peopleId[item.url] = item.name;
          }
        }
      });
  }
  // console.log(filmChars);
  // console.log(peopleId);
  printNames(filmChars, peopleId);
}

function printNames (list, obj) {
  for (const item of list) {
    console.log(obj[item]);
  }
}
main();
