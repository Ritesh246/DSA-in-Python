# Infinite recursion

def func(x,N):
    print(x)
    func(x,N)
func(15,4)