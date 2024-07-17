# Write a Program to remove Duplicate Element from a List

def Remove_Duplicat(l):
  empty_list = []
  for i in l:
    if i not in empty_list:
      empty_list.append(i)
  return empty_list
l = [2,3,4,5,6,5,4,3,2]
result = Remove_Duplicat(l)
print(result)