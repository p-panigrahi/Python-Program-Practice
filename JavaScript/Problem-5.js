// # Write a program to convert kelometer to mills
const prompt = require("prompt-sync")();

const kil = parseInt(prompt("Enter Any Number: "));
const miles = 0.621371;
const totalResult = kil * miles;
console.log(totalResult);
