// Write a Program to find the Vowels from string

const str = "PRABHUDUTTA";
var vowel = [];
var count = 0;
for (let i = 0; i < str.length; i++) {
  if (
    str[i].toLowerCase() == "a" ||
    str[i].toLowerCase() == "e" ||
    str[i].toLowerCase() == "i" ||
    str[i].toLowerCase() == "o" ||
    str[i].toLowerCase() == "u"
  ) {
    count = count + 1;
    vowel.push(str[i]);
  }
}
console.log(vowel);
console.log(count);
