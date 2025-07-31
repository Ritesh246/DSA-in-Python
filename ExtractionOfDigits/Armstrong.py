val=int(input("Enter a number to check armstrong or not:"))
num=val
rev=0
power=len(str(val))
while num>0:
    lastDig=num%10
    rev=rev+lastDig**power
    num=num//10
if(val==rev):
    print(f"The num {val} is Armstrong number")
else:
    print("Not an armstrong number")







