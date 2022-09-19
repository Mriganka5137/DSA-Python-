def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        small_power = power(x, n//2)
        return small_power * small_power
    else:
        small_power = power(x,n//2)
        return x * small_power * small_power
print(power(25,2))
