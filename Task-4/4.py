#This program checks if the inputted number is a palindrome or not
n=int(input("Enter the number: "))
rev=0
n1=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if n1==rev:
    print("True")
else:
    print("False")
    
