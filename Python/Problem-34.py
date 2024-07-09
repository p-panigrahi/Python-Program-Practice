# Write a Program To input a Character , if input character is uppercase then convert into lower case and its uppercase then convert into lowr

char = input("Enter Any Character: ")
if char >= "A" and char <= "Z":
  value = ord(char)
  value = value + 32
  print(chr(value))
elif char >= "a" and char <= "z":
  value = ord(char)
  value = value - 32
  print(chr(value))
else:
  print(f"{char} is not a Alphabate")