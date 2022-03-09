import numpy as np
s=int(input("Enter size:"))
for i in range(s):
    a = int(input("Enter 1st array's element:"))
    l1=[]
    l1.append(a)
x=np.array(l1)
for i in range(s):
    b = int(input("Enter 2nd array's element:"))
    l2=[]
    l2.append(b)
y=np.array(l2)
array_equal = np.allclose(x,y)
print(array_equal)
