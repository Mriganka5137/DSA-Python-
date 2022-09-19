def Convert(str,i):
    if i < 0:
        return 0
    c = str[i]
    n = int(c)
    # order = len(str)-1-i
    # return n*(10**order) + Convert(str,i-1)
    return n + Convert(str,i-1)*10
str = "0"
i=len(str)-1
print(Convert(str,i))