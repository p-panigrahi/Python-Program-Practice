// # Write a program to calculate the area of traingle
const prompt = require("prompt-sync")()
const base = parseFloat(prompt("Enter Any Number: "));
const height = parseFloat(prompt("Enter Any Number: "));
const traingle = 0.5 * base * height;
console.log(traingle);
