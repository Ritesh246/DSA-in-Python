val=int(input("Enter a number:"))
n=val
if n==0 or n==1:
    print("The number {n} is not a prime number")
    exit()
for i in range(2,(n//2)+1):
    if(n%i==0):
        print(f"The given number {n} is not a Prime number")
        exit()
print(f"The given number {n} is a Prime number")












