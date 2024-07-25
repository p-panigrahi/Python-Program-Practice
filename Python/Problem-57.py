# Write a Python program to Covert a List into a String
def list_to_string(l):
  str1 = " "
  # for i in l:
  #   str1 += i
  return str1.join(l)
l1 = ["Apple","Mango","Aroplen","Naruto"]
result = list_to_string(l1)
print(result)