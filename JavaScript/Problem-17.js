// # Write a Program to print the Armstrong Number
const prompt = require("prompt-sync")();
const number = prompt("Enter Any Number: ");
var temp = number;
const number_length = temp.length;
console.log(number_length)
var s = 0;
while (temp > 0) {
  let remender = temp % 10;
  s += remender ** number_length;
  temp = parseInt(temp / 10)
}

if (s == number) {
  console.log(`${number} is a Amstrong Number`);
} else {
  console.log(`${number} is not a Armstrong Number`);
}
