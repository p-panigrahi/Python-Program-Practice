// # Write a Python Program to Check a Number Is Fibonacci Number Or not

const is_perfect_Squre = (x) => {
  let s = parseInt(Math.sqrt(x));
  return s * s === x;
};

const is_fib = (num) => {
  return 5 * num * num + 4 || 5 * num * num - 4;
};
number = 34;
if (is_fib(number)) {
  console.log(`${number} is Fibonacci`);
} else {
  console.log("False");
}
