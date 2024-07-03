# Write a Program to Check The Given Number is Even Or ODD
number = int(input("Enter Your Number: "))
if number < 0:
  print(f"{number} is nagitive Plese Enter only Positive Number")
elif number % 2 == 0:
  print(f"{number} is Even")
else:
  print(f"{number} is ODD")