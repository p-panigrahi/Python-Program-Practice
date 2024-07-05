# Write a program to print all prime number in a intervial
lower = int(input("Enter Any Number: "))
upper = int(input("Enter Any Number: "))

for i in range(lower , upper+1):
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      print(i)