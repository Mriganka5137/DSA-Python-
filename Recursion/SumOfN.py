def sum_of_n(n):
    if(n == 0):
        return 0
    small_output = sum_of_n(n-1)
    output = n + small_output
    return output



n = int(input())
print(sum_of_n(n))