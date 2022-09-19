def power_of_number(n,m):
    if m == 0:
        return 1
    small_output = power_of_number(n,m-1)
    output= n * small_output
    return output


n=int(input())
m=int(input())
print(power_of_number(n,m))