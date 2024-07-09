# Write a Program to find the Factor Of a Number

num = int(input("Enter Any Number: "))

for i in range(1 , num+1):
  if num % i == 0:
    print(i)