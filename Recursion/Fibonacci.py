def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

n=100
print(fibo(n))

# 0,1,1,2,3,5,8,13,21,34