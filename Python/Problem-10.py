# Write a Program To Find The Prime Number
# def is_prime(number):
#   if number <= 1:
#     return False
#   for i in range(2, int(number**0.5) + 1):
#     if number % i == 0:
#       return False
#   return True
# def print_prime_number(num1):
#   # print(f"The Prime number Print {up_to}")
#   for num in range(2, num1+1):
#     if is_prime(num):
#       print(num ,end=" ")
#   print() 
# result = int(input("Enter Any Numbetr: "))
# print_prime_number(result)
def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, int(number ** 0.5)+1):
    if number % i == 0:
      return False
  return True
def print_prime_number(num1):
  print(f"Print Prime Number Up_to {num1}")
  for num in range(2, num1+1):
    if is_prime(num):
      print(num, end=" ")
  print()
number = int(input("Enter Any Number : "))
print_prime_number(number)