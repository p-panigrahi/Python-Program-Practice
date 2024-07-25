// Write a Program to find the Duplicate value in an array

const arr = [1, 22, 3, 4, 22, 44, 3, 4];
const result = arr.filter((value, index, arr) => arr.indexOf(value) !== index);
console.log(result);
