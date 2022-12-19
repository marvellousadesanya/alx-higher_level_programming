#!/usr/bin/node

let args = process.argv
args.sort(function(a,b) {
	return a - b;
});

if (args.length <= 2) {
  console.log(0);
} else {
    console.log(args[args.length - 2]);
}
