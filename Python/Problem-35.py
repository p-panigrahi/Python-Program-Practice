# Write a Program input a number and count number of even number digits and count number of odd number digits

num = int(input("Enter Any Number: "))
even_count = 0
odd_count = 0
while num > 0:
  rem = num % 10
  if rem % 2 == 0:
    even_count += 1
  else:
    odd_count += 1
  num //= 10
print(f"Even number count is {even_count}") 
print(f"Even number count is {odd_count}") 