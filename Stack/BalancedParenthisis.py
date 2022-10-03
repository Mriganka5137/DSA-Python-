
from sys import stdin


def isBalanced(expression) :
    data = []
    for ele in expression:
        if ele in '([{':
            data.append(ele)
        elif ele is ')':
            if(not data or data[-1] != '('):
                return False
            data.pop()
        elif ele is ']':
            if(not data or data[-1] != '['):
                return False
            data.pop()
        elif ele is '}':
            if(not data or data[-1] != '{'):
                return False
            data.pop() 
    if not data:
        return True
    return False














#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
