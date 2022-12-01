import sys

def countMinStepsToOne(n):
  
  if n == 0:
    return 0
  
  minsteps = [0]*( n + 1)
  minsteps[1] = 0

  for i in range(2, n+1):
    substractOne = minsteps[i - 1]
    divideByTwo = sys.maxsize
    divideByThree = sys.maxsize

    if i % 2 == 0:
      divideByTwo = countMinStepsToOne( n // 2)
    
    if i % 3 == 0:
      divideByThree = countMinStepsToOne(n // 3)
    
    ans = min(substractOne, divideByThree, divideByTwo)
    minsteps[i] = 1 + ans
  return minsteps[n]
