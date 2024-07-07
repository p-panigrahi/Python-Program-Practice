//  Write a Program To Check a number is Positive , Nagitive or Zero
// const prompt = require("prompt.sync")();
const prompt = require("prompt-sync")();


var number = parseInt(prompt("Enter Any Number: "));
if (number < 0) {
  console.log("Number Is Nagitive");
} else if (number === 0) {
  console.log("Number Is Zero");
} else {
  console.log("Number Is Positive ");
}
