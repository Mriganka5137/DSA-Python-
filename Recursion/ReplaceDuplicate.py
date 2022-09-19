def ReplaceDuplicate(s):
    if len(s)==1:
        return s
    smallerOutput = ReplaceDuplicate(s[1:])
    if s[0] == smallerOutput[0]:
        return smallerOutput
    else:
        return s[0] + smallerOutput
s="coodinnnggsssssss"
print(ReplaceDuplicate(s))