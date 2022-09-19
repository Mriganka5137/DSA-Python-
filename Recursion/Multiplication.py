def Multiplication(n,m):
    if m ==0:
        return 0
    a=Multiplication(n, m-1)
    return n + a
print(Multiplication(0,6))