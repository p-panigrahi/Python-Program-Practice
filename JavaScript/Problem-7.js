// # Write a Program to Check The Given Number is Even Or ODD
const prompt = require("prompt-sync")();

var number = parseInt(prompt("Enter Any Number: "));
if (number <= 0) {
  console.log("Please enter Positive Number");
} else if (number % 2 == 0) {
  console.log(`${number} is Even`);
} else {
  console.log(`${number} is ODD`);
}
