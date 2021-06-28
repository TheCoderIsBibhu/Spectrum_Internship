# 7  Given an array ‘a[ ]’ and a value ‘k’, find if there is a triplet in the array whose sum
# is equal to the value.

a=[]
n=int(input("Enter the range of array: "))
print("Enter the elements: ")
for i in range(n):
    a.append(int(input()))
k=int(input("Enter the particuar number:")) 
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            if (a[i]+a[j]+a[l]==k):
                print(a[i],a[j],a[l])



