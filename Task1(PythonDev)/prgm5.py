# 5. Given a nber ‘n’ find the first n perfect numbers

n=int(input("How many perfect Number you want: "))
a=[4]
k=0
for i in range(1,100000):
    sum=0
    for j in range(1,int(i/2)+1):
        if i%j==0:
            sum=sum+j
    if sum==i:
        k+=1
        print(i,end=",")
        if k==n:
            break
print()



