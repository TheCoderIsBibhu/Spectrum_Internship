#2 Given a number find the number of zeros in the factorial of the number. 

num=int(input("Enter a Number: "))
i=0
while num!=0:
    i+=int(num/5)
    num=num/5

print("The Number of zeros in factorial of the number is ",i)