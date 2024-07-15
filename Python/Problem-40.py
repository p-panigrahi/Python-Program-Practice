# Write a Program to count the number of digits present in a number
num = int(input("Enter Any Number: "))
count = 0
while num != 0:
  num = num // 10
  count = count + 1
print(count)