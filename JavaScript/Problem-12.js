// # Write a program to print all prime number in a intervial
const prompt = require("prompt-sync")();
const is_Prime = (number) => {
  if (number <= 1) {
    return 0;
  } else {
    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
        return false;
      }
    }
    return true;
  }
};
const print_prime = (Up_To) => {
  console.log(`Print The Prime Number ${Up_To}`);
  for (let j = 2; j <= Up_To; j++) {
    if (is_Prime(j)) {
      console.log(j);
    }
  }
};
number = parseInt(prompt("Enter Any Number: "));
print_prime(number);
