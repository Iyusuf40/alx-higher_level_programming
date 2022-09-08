#!/usr/bin/node
function callMeMoby (x, fx) {
  for (let y = 0; y < x; y++) {
    fx();
  }
}
exports.callMeMoby = callMeMoby;
