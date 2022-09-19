def SumOfDigit(n):
    if n%10 == n:
        return n
    lastDigit = n%10
    nextDigits = n//10
    return lastDigit + SumOfDigit(nextDigits)
n=2564856
print(SumOfDigit(n))