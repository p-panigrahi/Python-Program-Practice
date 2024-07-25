# Write a Program to Count a Occurence of a element in a list

l = [1,2,3,4,5,5,5,5,6,7]
el = 5
count = 0
for i in l:
  if i == el:
    count = count+1
print(count)