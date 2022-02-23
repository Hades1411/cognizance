#this 2 dimentional list contains a student's name and their marks
size=int(input("How many students are there?: "))
l = [[(i) for j in range(3)] for i in range(size)]

for i in range(0,size):
    name=input("Enter student name: ")
    marks=input("Enter their marks: ")
    l[i]=[i+1,name,marks]
print("Rollno\tName\tMarks")
for i in l:
    for j in i:
        print(j, end='\t')
    print()

print("2nd record")
for i in l[1]:
    print(i,end='\t')
