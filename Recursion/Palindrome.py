def Palindrome(s,si,ei):
    if si >= ei:
        return True
    if s[si] != s[ei]:
        return False
    return Palindrome(s,si+1,ei-1)
s="aaaaaaa"
print(Palindrome(s,0,len(s)-1))