 // Python Program for n-th Fibonacci number
const prompt = require("prompt-sync")()
const fib = (num)=>{
  if (num < 2){
    return num
  }else{
    return fib(num-1) + fib(num-2)
  }
}
const number = parseInt(prompt("Enter Any Number: "))
if (number < 0){
  console.log("Pleaase Enter Positive Number")
}else{
  for (let i = 0; i < number; i++){
    console.log(fib(i))
  }
}