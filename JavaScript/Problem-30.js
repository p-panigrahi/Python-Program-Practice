// Write a Program to print prime number
const num = 66;
if (num <= 1) {
  console.log("Not a Prime number");
} else {
  for (let i = 2; i < num; i++) {
    if (num % 2 === 0) {
      var result = `${num} is not a prime number`;
      break;
    } else {
      var result = `${num} is a prime number`;
    }
  }
  console.log(result);
}
