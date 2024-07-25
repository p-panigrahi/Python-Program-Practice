# Write a Python Program to Find the Second Largest Number in a List

l1 = [88 , 100 , 1,2,3,4,34,45,56,56,56,56,67,67,67]
l2 = list(set(l1))
l2.sort()
print(f"The Second Largest number is {l2[-2]}")