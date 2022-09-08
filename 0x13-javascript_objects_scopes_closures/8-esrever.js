#!/usr/bin/node
exports.esrever = function (list) {
  const res = [];
  for (let x = (list.length - 1); x >= 0; x--) {
    res.push(list[x]);
  }
  return res;
};
