def PairStar(str,i):
    if i == len(str) - 1:
        return str[i]
    if str[i] == str[i+1]:
        return str[i] + '*' + PairStar(str, i+1)
    else:
        return str[i] + PairStar(str,i+1)
str="aaaa"
print(PairStar(str,0))