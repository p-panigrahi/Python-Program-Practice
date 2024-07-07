# Write A Program To Find The Factorial Of Number

# number = int(input("Enter Any Number: "))
# fact = 1
# if number < 0:
#   print("Factorial Is Does not Exist")
# elif number == 0:
#   print(f"{number} Factorial Is 1")
# else:
#   for i in range(1 , number+1):
#     fact = fact * i
#   print(fact)

# Using Recoursion
def factorial(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return n * factorial(n -1)
number = int(input("Enter Any number: "))
print(factorial(number))