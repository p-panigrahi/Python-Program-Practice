// # Write a Python Program to Print The Fibonacci Series
const prompt = require("prompt-sync")();
var a = 0;
var b = 1;
var c = 0;
var sum = a + b
var number = parseInt(prompt("Enter Any Number: "));

if (number == 1) {
  console.log(a);
} else {
  console.log(a);
  console.log(b);
  for (let i = 2; i < number; i++) {
    c = a + b;
    a = b;
    b = c;
    sum = sum + c
    console.log(c);
  }
  console.log(`Sum Of Fib is ${sum}`)
}
