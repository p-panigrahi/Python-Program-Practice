// # Python Program for Sum of squares of first n natural numbers
const prompt = require("prompt-sync")()
const square_of_first_number = (n)=>{
  let sum = 0;
  for (let i = 0; i <= n; i++){
    sum = sum + (i * i)
  }
  return sum
}
const number = parseInt(prompt("Enter Any Number: "))
console.log(square_of_first_number(number))