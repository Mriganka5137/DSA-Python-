def ReplacePi(s):
    if len(s) == 1 or len(s) == 0:
        return s
    if s[0] == 'p' and s[1] == 'i':
        smallerOutput = ReplacePi(s[2:])
        return "3.14" + smallerOutput
    else:
        smallerOutput = ReplacePi(s[1:])
        return s[0] + smallerOutput

print(ReplacePi("abcpibpippi"))