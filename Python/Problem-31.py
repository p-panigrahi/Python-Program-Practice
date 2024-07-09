# Python Program to Split the array and add the first part to the end

arr = [10,34,56,78,90]
position = 2
x = arr[:position]
print(x)
y = arr[position:]
print(y)
y.extend(x)
print(y)
