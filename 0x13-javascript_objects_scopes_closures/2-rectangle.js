#!/usr/bin/node

module.exports = class Rectangle {
  // class constructor
  constructor (w, h) {
    // check if w and h are positive integers
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      // initialize instance attributes
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }
};
