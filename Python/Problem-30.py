# Python Program for Reversal algorithm for array rotation

def arr_roation(arr,d):
  c = (arr[d:] + arr[:d])
  return c
arr = [1,2,3,4,5,6,7,8,9]
d = 3
print(arr_roation(arr,d))