#!/usr/bin/node

exports.esrever = function (list) {
  const Listreversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    Listreversed.push(list[i]);
  }
  return Listreversed;
};
