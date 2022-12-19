#!/usr/bin/node

let size = Number(process.argv[2]);

if (!Number.isInteger(size) || !size) {
  console.log('Missing size');
}

for (let j = 1; j < size; j++) {
    console.log('X'.repeat(size));
}
