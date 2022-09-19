def RemoveX(s,x):
    l = len(s)
    if l == 0:
        return s
    smallerOutput = RemoveX(s[1:], x)
    if s[0] == x:
        return smallerOutput
    else:
        return s[0] + smallerOutput

s = "xxxx"
print(RemoveX(s,'x'))