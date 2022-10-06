
from sys import stdin

def countBracketReversals(inputString) :

    # Your code goes here
  if len(inputString)  % 2 != 0:
    return -1
  
  count = 0
  arr = []
  for ele in inputString:
    if ele == '{':
      arr.append(ele)
    else:
      if len(arr) == 0:
        count+=1
      elif arr[-1] == '{':
        arr.pop()
      else:
        count+=1
  if len(arr) != 0:
    count += len(arr)//2
  return count








#main
print(countBracketReversals(stdin.readline().strip()))
