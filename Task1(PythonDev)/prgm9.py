# 9. Given an array ‘a[ ]’ of integers and an integer ‘n’.
#  You have to print the n’th smallest integer in the array.

a=[]
temp=0
size=int(input("Enter the range of array:"))
print("Enter the elements of array: ")
for i in range(size):
    a.append(int(input()))
n=int(input("Enter the what times smallest number you want to find:  "))
k=a[0]
for i in range(size):
    for l in range(i+1,size):
        if a[i]>a[l]:
            temp = a[i]   
            a[i] = a[l]    
            a[l] = temp
print("The ",n,"th smallest number of array is",a[n-1])