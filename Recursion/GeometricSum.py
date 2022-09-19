def GeometricSum(n):
    if n == 0:
        return 1
    return 1/(2**n) + GeometricSum(n-1)
print()
a=GeometricSum(2)
print("{0:.5f}".format(a))