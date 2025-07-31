val=int(input("Enter a number to find it's length:-"))
num=val
count=0
if num==0:
    count=1
    print(f"The length of given number is:-{count}")
    
while num!=0:
    num=num//10
    count+=1
print(f"The length of given number is:-{count}")








