# Python Program for Sum of squares of first n natural numbers

def squre_of_first_number(n):
  s = 0
  for i in range(1,n+1):
    s = s + (i * i)
  return s
print(squre_of_first_number(7))