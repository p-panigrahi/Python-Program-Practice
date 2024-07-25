// Write a Program to find max and min value in a given Array in javaScript

const num = [1,2,3,4,5];
const max_value = num.reduce((pre , cur)=>{
  return pre < cur ? pre : cur;
})
console.log(max_value);
