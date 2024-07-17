# write a Program in pythonW to check if a Sequence is a Palindrom or not
def is_Palindrom(sequence):
  reverse_sequence = sequence[::-1]
  return reverse_sequence == sequence
sequence = input("Enter Any Sequence: ")
if is_Palindrom(sequence):
  print(f"The Sequence {sequence} is a Palindrom")
else:
  print(f"The Sequence {sequence} is not a Palindrom")
