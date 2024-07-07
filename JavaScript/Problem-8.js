// # Write a Program To Find The Leap Year
const prompt = require('prompt-sync')()

var year = parseInt(prompt("Enter Any Year: "))
if (year % 400 === 0 && year % 100 === 0){
  console.log(`${year} is a Leap Year`)
}
if (year % 4 === 0 && year % 100 !== 0){
  console.log(`${year} is a leap Year`)
}else{
  console.log(`${year} is not a Leeap Year`)
}