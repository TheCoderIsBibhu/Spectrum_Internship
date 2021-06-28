#3 Given an integer ‘n’ find all prime numbers from 1 to n. 

num=int(input("Enter a Number: "))
print("The prime numbers within ",num,"is:",end=" ")
for i in range(2, num + 1):
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           print(i,end=",")
print()