r=5
t=r-1 #changes the number of spaces in each row
for i in range(0,r):
    for j in range(0,t):
        print(end=" ")
    t-=1
    for j in range(0,i+1):
        print("* ",end="")     
    print("")
