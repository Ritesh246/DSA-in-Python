val=int(input("Enter a number:"))
n=val
if n==0:
    print("1")
while n>0:
    lastDigit=n%10
    print(lastDigit)
    n=n//10
    







