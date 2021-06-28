# 8. Write a python program to display the  star pattern

for rows in range(5,0,-1):
    for cols in range(0,5-rows):
        print(end=" ")
    for cols in range(0,rows):
        print("*",end=" ")
    print()
for rows in range(2,6):
    for cols in range(0,5-rows):
        print(end=" ")
    for cols in range(0,rows):
        print("*",end=" ")
    print()