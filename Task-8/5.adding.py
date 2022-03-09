import numpy as np
n=int(input("Size: "))
a1=[]
a2=[]
for i in range(n):
    a=int(input("Enter 1st array element:"))
    a1.append(a)
for i in range(n):
    b=int(input("Enter 2nd array element:"))
    a2.append(b)

arr1 = np.array(a1)
arr2 = np.array(a2)

print("1st array : ", arr1)
print("2nd array : ", arr2)
arr = np.add(arr1, arr2)
print("Added array: ", arr)
