#!/usr/bin/node
/* displays the status code of a request to url passed as arg */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, resp, body) => {
  if (!err) {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
