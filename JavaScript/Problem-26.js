// How to find even and odd number in array

const arr = [1, 2, 3, 4, 5, 6];
var even_val = [];
var odd_val = [];
for (let i = 1; i <= arr.length; i++) {
  if (i % 2 === 0) {
    even_val.push(i);
  } else {
    odd_val.push(i);
  }
}
console.log(arr);
console.log(even_val);
console.log(odd_val);
