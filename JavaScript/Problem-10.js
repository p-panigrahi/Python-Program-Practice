// Write a Program To Cheak A Input Number Is Prime Or Not
const is_Prime = (number) => {
  if (number <= 1) {
    console.log("Enter Positive Number");
  }
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
};

var num = 4;
if (is_Prime(num)) {
  console.log(`${num} is Prime Number`);
} else {
  console.log(`${num} is Not Prime`);
}
