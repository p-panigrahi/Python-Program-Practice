# Write a Program to count the number of accurence of a Character in string

string = input("Enter Any String: ")
any_chr = input("enter Any Char: ")
count = 0
for i in string:
  if i == any_chr:
    count += 1
print(count)