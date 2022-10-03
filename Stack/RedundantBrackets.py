
from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
  arr = []
  count = 0
  for ele in expression:
    if ele == ')':
      arr = check(arr)
      

    else:
      arr.append(ele)


def check(arr):
  count = 0
  while arr[len(arr)-1] != '(':
    arr.pop()
    count+=1
  if count == 0:
    return True
  else:
    arr.pop()
    return arr
  

#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
