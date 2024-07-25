# Write a Program to interchange first and last elements in a list

def interchange(elem):
  elem[0] , elem[-1] = elem[-1] , elem[0]
  return elem
elem = ["Aman","Rabi","Rajhu","Rakesh","Sipun","Bira"]
result = interchange(elem)
print(result)