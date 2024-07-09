# Python Program to Swap Two Elements in a List

def swap_any_element(list , post1 , post2):

  list[post1] , list[post2] = list[post2] , list[post1]
  return list
list = [22,34,56,78,89]
post1 = 3
post2 = 4
print(swap_any_element(list , post1 , post2))