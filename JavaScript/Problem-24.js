// How to find second largest value , and remove first largest value in array

const num = [1, 2, 3, 4, 5, 6];
const largest_value = (arr) => {
  const max_value = Math.max(...arr);
  const index = arr.indexOf(max_value);
  arr.splice(index, 1);
  const second_max_value = Math.max(...num);
  return second_max_value;
};
const result = largest_value(num);
console.log(result);
