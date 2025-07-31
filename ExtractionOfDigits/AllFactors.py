#My Way

# val=int(input("Enter a number to get all factors:"))
# num=val
# i=1
# print("Using while loop")
# while i<=num:
#     if(num%i==0):
#         print(i)
#     i+=1
# print("Using for loop")
# for i in range(1,num+1):
#     if(num%i==0):
#      print(i)    

val=int(input("Enter a number:"))
n=val
result=[]
for i in range(1,(n//2)+1):
    if n%i==0:
        result.append(i)
result.append(n)
print(result)





