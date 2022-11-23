
import math
import sys


def minSquare(n, dp):
  if n == 0:
    return 0
  
  ans = sys.maxsize
  root = int(math.sqrt(n))
  
  for i in range(1, root + 1):
    
    checkValue = n - (i**2)
    
    if(dp[checkValue] == -1):
      smallAns = minSquare(checkValue, dp)
      dp[checkValue] = smallAns
      currentAns = 1 + smallAns
    
    else:
        currentAns = 1 + dp[checkValue]
    
    ans = min(currentAns, ans)
  return ans
  
  
    


n = int(input())
dp = [-1 for i in range(n + 1)]
ans = minSquare(n, dp)
print(ans)