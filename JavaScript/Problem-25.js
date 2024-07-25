// Write a Program To find the Missing number in given interger

const num = [1, 2, 3, 6, 7, 9];
var missing_Number = [];
const find_number = (arr) => {
  const min_value = Math.min(...arr);
  const max_value = Math.max(...arr);
  for (let i = min_value; i < max_value; i++) {
    if (arr.indexOf(i) < 0) {
      missing_Number.push(i);
    }
  }
  return missing_Number;
};
console.log(find_number(num));
