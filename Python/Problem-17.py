# Write a Program to print the Armstrong Number

number = int(input("Enter Any Number: "))
temp = number
number_length = len(str(temp))
s = 0
while temp > 0:
  remender = temp % 10
  s += remender ** number_length
  temp = temp // 10

if s == number:
  print(f"{number} is a Amstrong Number")
else:
  print(f"{number} is not a Armstrong Number")

