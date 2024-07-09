# Write a Program to display power of 2 using annmous function

nTh_Tearm = int(input("Enter Any Number: "))

result = list(map(lambda x : 2 ** x, range(nTh_Tearm + 1)))
print(result)
for i in range(nTh_Tearm+1):
  print(result[i])