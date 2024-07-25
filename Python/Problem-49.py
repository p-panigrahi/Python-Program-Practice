# Write a Python Program to Swap Two Elemnt in a List

def swap_list_elem(l , post1 , post2):
  l[post1] , l[post2] = l[post2] , l[post1]
  return l
l = [1,2,3,4,5]
post1 = 1
post2 = 4
result = swap_list_elem(l , post1-1 , post2-1)
print(result)