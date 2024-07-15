# Write a Program To Reverse a Number

num = int(input("Enter any Number"))
rev = 0
while num != 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10
print(f"The Rev is {rev}")
