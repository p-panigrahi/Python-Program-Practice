# Write a Program to print the duplicate list into a exzisting list
def print_Duplicate(l):
  main_list = []
  dup_list = []
  for i in l:
    if i not in main_list:
      main_list.append(i)
    else:
      dup_list.append(i)
  return main_list , dup_list



l1 = [1,2,3,4,5,5,6,7,7,8]
result1 , result2 = print_Duplicate(l1)
print(result1)
print(result2)