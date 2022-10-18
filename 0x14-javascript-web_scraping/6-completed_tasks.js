#!/usr/bin/node
/* gets an api and builds an object literal */

const request = require('request');

const url = process.argv[2];
const obj = {};

request(url, (err, resp, body) => {
  if (!err) {
    const data = JSON.parse(body);
    for (const item of data) {
      if (obj[item.userId]) {
        if (item.completed) {
          obj[item.userId] += 1;
        }
      } else {
        if (item.completed) {
          obj[item.userId] = 1;
        }
      }
    }
  }
  console.log(obj);
});
