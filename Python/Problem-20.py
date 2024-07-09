# // Python Program for n-th Fibonacci number

def fib(num):
  if num <= 0:
    print("Enter Correct Number")
  elif num == 1:
    return 0
  elif num == 2:
    return 1
  else:
    return fib(num-1) + fib(num-2)
  
number = int(input("Enter Any number: "))
if number < 0:
  print("Plese Enter Positive number")
else:
  for i in range(1,number+1):
    print(fib(i))