def StairCase(n):
    if(n==1 or n==2):
        return n
    if n == 3:
        return 4
    Recursive1 = StairCase(n-1)
    Recursive2 = StairCase(n-2)
    Recursive3 = StairCase(n-3)

    return Recursive1 + Recursive2 + Recursive3
print(StairCase(5))