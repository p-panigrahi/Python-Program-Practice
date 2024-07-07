// Write a Program To Find the Factorial Of a Number
const prompt = require("prompt-sync")();

// const number = parseInt(prompt("Enter Any Number: "));
// let fact = 1;
// if (number < 0) {
//   console.log("Factorial is not Exist");
// } else if (number === 0) {
//   console.log(`${0} factorial is 1`);
// } else {
//   for (let i = 1; i <= number; i++) {
//     fact = fact * i;
//   }
//   console.log(fact);
// }

// Using Recousion
const factorial = (num) => {
  if (num == 0) {
    return 1;
  } else if (number < 0) {
    return 0;
  } else {
    return num * factorial(num - 1);
  }
};
const number = parseInt(prompt("Enter Any number: "));
console.log(factorial(number));
