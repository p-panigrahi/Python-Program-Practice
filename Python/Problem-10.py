# Write a Program To Find The Prime Number
number = int(input("Enter Your Number: "))
if number == 0:
  print("Enter Positive Number")
  if number > 1:
    for i in range(2,number):
      if number % i == 0:
          print(f"{i} is Not a Prime Number")
          break
    else:
      print("{i} is Prime Number")