// Write a Program To Calculate The Simple Intrest
const prompt = require("prompt-sync")();
var p = parseFloat(prompt("Enter Any Number: "));
var r = parseFloat(prompt("Enter Any Number: "));
var t = parseInt(prompt("Enter Any Number: "));

const si = (p * r * t) / 100;
console.log("The Simple Intrest is : ", si);
