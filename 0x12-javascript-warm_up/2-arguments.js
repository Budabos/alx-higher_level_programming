#!/usr/bin/node
const argv = 'process.argv.length';
if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
