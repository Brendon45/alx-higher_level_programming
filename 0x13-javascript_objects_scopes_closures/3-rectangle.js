#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect; // declare var to act as container for printing charcaters
    for (let i = 0; i < this.height; i++) {
      // let the variable be an empty string
      rect = '';
      for (let j = 0; j < this.width; j++) {
        // append the X char to the variable in each iteration
        rect += 'X';
      }
      console.log(rect);
    }
  }
};
