def CountZeros(n):
    # if n==0:
    #     return 1
    # if n//10 == 0:
    #     return 0
    if n % 10 == n:
        if n==0:
            return 1
        return 0
    if n % 10 == 0:
        return 1 + CountZeros(n//10)
    else:
        return CountZeros(n//10)
n=int(input())
print(CountZeros(n)) 