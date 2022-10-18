#!/usr/bin/node
/* displays the status code of a request to url passed as arg */

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    console.log('code:', response.statusCode);
  }
});
