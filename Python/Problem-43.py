# Write a Program to find the Number is Prime or Not
def is_Prime(num):
  if num <= 1:
    return False
  for i in range(2 , int(num ** 0.5)+1):
    if num % i == 0:
      return False
  return True
number = int(input("Enter Any number: "))
if is_Prime(number):
  print(f"{number} is a Prime number")
else:
  print(f"{number} is a not Prime")