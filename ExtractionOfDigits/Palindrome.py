val=int(input("Enter number to check whether palindrome or not:-"))
num=val
rev=0
if num==0:
    print("Entered number is palindrome")
    exit()
while num>0:
    lastDigit=num%10
    rev=(rev*10)+lastDigit
    num=num//10
if val==rev:
    print("The number is Palindrome")
else:
    print("The number is not a Palindrome")
    
    











