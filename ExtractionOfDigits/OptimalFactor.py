from math import sqrt
val=int(input("Enter a number:"))
n=val
result=[]
for i in range(1,sqrt(n)+1):
    if n%i==0:
        result.append(i)
        if n%i!=i:
            result.append(n//i)
print(result)
        










