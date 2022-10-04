#!/usr/bin/node

let secondLargest = 0;
const args = process.argv.slice(2);

if (args.length > 1) {
  args.sort();
  secondLargest = args[args.length - 2];
}
console.log(secondLargest);
