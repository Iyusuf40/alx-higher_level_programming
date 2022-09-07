#!/usr/bin/node
const list = process.argv;
const ps = parseInt;
if (list.length < 4) {
  console.log(0);
} else {
  let small = ps(list[2]) <= ps(list[3]) ? ps(list[2]) : ps(list[3]);
  let big = ps(list[3]) >= ps(list[2]) ? ps(list[3]) : ps(list[2]);
  for (let index = 2; index < list.length; ++index) {
    if (ps(list[index]) > big) {
      const save = big;
      big = ps(list[index]);
      if (save > small) {
        small = save;
      }
    }
    if (ps(list[index]) > small && list[index] < big) {
      small = ps(list[index]);
    }
  }
  console.log(small);
  console.log(big);
}
