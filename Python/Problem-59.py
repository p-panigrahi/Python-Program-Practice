# Write a Progrm to find the largest number in a list
l1 = [10,40,30,50,100,2000,1000,2000 , 200 , 300]
l2 =  list(set(l1))
l2.sort()
print(l2[-1])
print(l2)