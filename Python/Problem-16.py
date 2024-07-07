# Write a Python Program to Print The Fibonacci Series 

a = 0
b = 1
# s = a +b
number = int(input("Enter Any Number: "))

if number == 1:
  print(a)
else:
  print(a)
  print(b)
  for i in range(2,number):
    c = a+b
    a = b
    b = c
    # s = s + c
    print(c)
  print(f"The sum of Fib is {s}")







