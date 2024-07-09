# Python program to interchange first and last elements in a list
def swap_element(l):

  list[0],list[-1] = list[-1],list[0]
  return list

list = [12,34,56,78,90]
print(swap_element(list))