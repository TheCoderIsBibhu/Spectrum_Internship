#4 Given an aay of integers ‘a[ ]’ find the greatest common divisor(GCD) of those
# numbers

a=[]
n=int(input("Enter the range of the array:"))
print("Enter the elements: ")
for i in range(0,n):
    a.append(int(input()))
b=a[0]
import math
for i in range(1,len(a)):
    s=math.gcd(b,a[i])
    b=s

print("GCD of the Numbers is :",b)
