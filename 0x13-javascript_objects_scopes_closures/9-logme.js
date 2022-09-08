#!/usr/bin/node
function logMe (item) {
  this.f = () => {
    console.log(logMe.prototype.count + ': ' + item);
    logMe.prototype.count++;
  };
  this.f();
}
logMe.prototype.count = 0;
exports.logMe = logMe;
