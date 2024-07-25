// 912. Sort an Array
// Given an array of integers nums, sort the array in ascending order and return it.
// You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
// Example 1:
// Input: nums = [5,2,3,1]
// Output: [1,2,3,5]
// Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5
// Constraints:
// 1 <= nums.length <= 5 * 104

function sortArray(nums) {
  // Case1
  if (nums.length < 2) {
    return nums;
  }
  // case2
  const meddle = Math.floor(nums.length / 2);
  const left = nums.slice(0, meddle);
  const right = nums.slice(meddle);

  return mearg(sortArray(left), sortArray(right));
}

function mearg(left, right) {
  const result = [];
  let i = 0;
  let j = 0;
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }
  while (i < left.length) {
    result.push(left[i]);
    i++;
  }
  while (j < right.length) {
    result.push(right[j]);
    j++;
  }
  return result;
}
const num = [-2, 3, -5];
const result2 = sortArray(num);
console.log(result2);
