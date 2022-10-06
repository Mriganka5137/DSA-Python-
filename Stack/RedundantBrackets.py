
from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
  arr = []
  count = 0
  for ele in expression:
    if ele == ')':
      i = len(arr) -1
      while(arr[i] != '('):
        arr.pop()
        count+=1
        i-=1
      if count <= 0:
        return True
      else:
        arr.pop()
        count=0
    else:
      arr.append(ele)

  

#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
