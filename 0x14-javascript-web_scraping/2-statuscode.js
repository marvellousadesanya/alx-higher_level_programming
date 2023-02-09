#!/usr/bin/node

const request = require('request');

const path = process.argv[2];

request(path, (error, response) => {
  console.log(`code: ${response.statusCode}`);
});
