# Write a Program To find a Aramstrong Number in an Intervial
lower = int(input("Enter Any Number: "))
upper = int(input("Enter Any Number: "))

for i in range(lower , upper+1):
  temp = i
  s = 0
  length = len(str(temp))
  while temp > 0:
    rem = temp % 10
    s += rem ** length
    temp  //=  10
  if s == i:
    print(i)