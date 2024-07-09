// # Program to print ASCII Value of a character
const prompt = require("prompt-sync")()
const ch = parseInt(prompt("Enter Any Character: "))
// const result = ch.charCodeAt() //To Find Character Value
const result = String.fromCharCode(ch)
console.log(result)