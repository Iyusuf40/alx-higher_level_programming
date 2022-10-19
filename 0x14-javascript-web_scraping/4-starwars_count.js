#!/usr/bin/node
/* displays the status code of a request to url passed as arg */

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    let count = 0;
    const data = JSON.parse(body);
    const list = data.results;
    let index = 0;
    for (index = 0; index < list.length; index++) {
      if (checkFor18(list[index].characters).length === 1) {
        count += 1;
      }
    }
    console.log(count);
  }
});

function checkFor18 (list) {
  return (
    list.filter((item) => {
      // return (item === 'https://swapi-api.hbtn.io/api/people/18/');
      return (item.includes('/18/'));
    }
    )
  );
}
