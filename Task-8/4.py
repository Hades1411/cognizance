import pandas as pd
s=input("Enter the string : ")
str=s.split()
series = pd.Series(str)
x = series.str.capitalize()
for i in x :
    print(i,end = " ")
print()

