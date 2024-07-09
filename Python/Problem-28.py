# Write a Program to find the Largest Element In An Array

def largest(arr,n):
  max = arr[0]
  for i in range(1, n):
    if arr[i] > max:
      max = arr[i]
  return max
arr = [1,2,3,4,5,6,7,8]
n = len(arr)
result = largest(arr,n)
print(result)