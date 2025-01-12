def FibonacciSeq(n):
    if(n==0):
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciSeq(n-2) + FibonacciSeq(n-1)
    
n = 5
for i in range(n):
    print(FibonacciSeq(i),end=" ")