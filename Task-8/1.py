import numpy as np
f_no=int(input("first: "))
l_no=int(input("last: "))
l=[]
for i in range(f_no,l_no+1):
    l.append(i)
a=np.array(l)
z=5
j=0
z0 = np.zeros(len(a) + (len(a)-1)*(z))
for i in range(0,len(z0),z+1):
    z0[i]=a[j]
    j=j+1
print(z0)

