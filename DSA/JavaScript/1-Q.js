// 1. Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.
// Example 1:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// function twoSum(nums, target) {
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = i + 1; j < nums.length; j++) {
//       if (nums[i] + nums[j] === target) {
//         return [[i, j]];
//       }
//     }
//   }
//   return [];
// }
// const num = [2, 7, 11, 15];
// const tar = 9;
// const result = twoSum(num, tar);
// console.log(result);
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for(let k = j+1; k < nums.length; k++){
        for (let l = k+1; l < nums.length; l++){
          if (nums[i] + nums[j] + nums[k] + nums[l] === target) {
            return [nums[i], nums[j], nums[k] , nums[l]];
          }
        }
      }
    }
  }
  return [];
}
const num = [1,0,-1,0,-2,2];
const tar = 0;
const result = twoSum(num, tar);
console.log(result);
