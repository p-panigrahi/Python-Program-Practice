# Write a Program to find Largest among Three Number
num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))
num3 = int(input("Enter Your Third Number: "))
if num1 > num2 and num1 > num3:
  print(f"{num1} is Grater Among Three Number")
elif num2 > num1 and num2 > num3:
  print(f"{num2} is Greater Among Three Number")
else:
  print(f"{num3} is Grater Among Three Number")