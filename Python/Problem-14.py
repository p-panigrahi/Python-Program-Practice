# Write A Program To Calculate The Simple Intrest

# Using Function
# def simple_Intrest(p,r,t):
#   print("The Princepal Amount",p)
#   print("The Interest rate",r)
#   print("The Time",t)

#   si = (p * r * t)/100
#   print("The si is :" , si)
#   return si
# simple_Intrest(30000,5,10)

# Using Normal Way
p = float(input("Enter Any Number: "))
r = float(input("Enter Any Number: "))
t = int(input("Enter Any Number: "))

si = (p * r * t)/100
print("The Simple Intrest is : ", si)