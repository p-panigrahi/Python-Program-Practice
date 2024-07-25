# Write a Python Program to print the prime number between 100 200
def prime(num):
  if num <= 1:
    return False
  for i in range(2 , int(num**0.5)+1):
    if num % i == 0:
      return False
  return True
def print_upto(start , end):
  print(f"Print prime number between {100} to {200}");
  for j in range(start,end+1):
    if prime(j):
      print(j , end=" ")
print(print_upto(100 , 200))
