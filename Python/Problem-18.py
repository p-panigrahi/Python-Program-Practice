# Write a Python Program to Check a Number Is Fibonacci Number Or not
import math
def is_perfect_square(x):
  s = int(math.sqrt(x))
  return s * s == x
def is_fibonacci(n):
  return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
number  = int(input("Enter Any Number: "))
if is_fibonacci(number):
  print(f"{number} is Fibnacci Number")
else:
  print(f"{number} is not a fibnacci number")