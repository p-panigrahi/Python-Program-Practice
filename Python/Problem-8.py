# Write a Program To Find The Leap Year
year = int(input("Enter Your Years: "))
if year % 400 == 0 and year % 100 == 0:
  print(f"This Is {year} Leap Year")
elif year % 4 == 0 and year % 100 != 0:
  print(f"This is {year} Leap Year ")
else:
  print("Not Leap Year")