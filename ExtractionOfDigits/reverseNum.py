val=int(input("Enter a number to reverse:"))
num=val
rev=0
if num==0:
    print("0")
    exit()
while num>0:
    lastD=num%10
    rev=(rev*10)+lastD
    num=num//10
print(f"The reverse number is {rev}")








