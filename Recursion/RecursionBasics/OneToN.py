# HEAD Recursion
# def func(i,N):
#     if i>N:
#         return
#     print(i)
#     func(i+1,N)
# func(1,4)

# Tail Recursion
def func(i,N):
    if i>N:
        return
    func(i+1,N)
    print(i)
func(1,4)