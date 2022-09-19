def ReplaceChar(s,a,x):
    l = len(s)
    if l == 0:
        return s
    smallerOutput = ReplaceChar(s[1:], a, x)
    if s[0] == a:
        return x + smallerOutput
    else:
        return s[0] + smallerOutput


s="sdfdhdk"
print(ReplaceChar(s,'a','x'))
