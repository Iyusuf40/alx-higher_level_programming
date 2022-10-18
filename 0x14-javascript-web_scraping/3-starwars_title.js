#!/usr/bin/node
/* displays the status code of a request to url passed as arg */

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (err, response, body) => {
  if (!err) {
    console.log(JSON.parse(body).title);
  }
});
