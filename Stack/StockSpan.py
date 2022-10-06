
from sys import stdin

def stockSpan(price, n) :
	#Your code goes here
  
  # if len(price) == 1:
  #   price.pop()
  #   price.append(1)
  #   return
  # ele = price[n-1]
  # i = n -2
  # count = 1
  # while(i >= 0):
  #   if ele > price[i]:
  #     count=count+1
  #     i-=1
  #   if ele < price[i]:
  #     break
  # price.pop()
  # stockSpan(price,n-1)
  # price.append(count)
  # return price

  S = [None] * n
  S[0] = 1
  for i in range(1,n,1):
    S[i] = 1
    j = i - 1
    while(j>=0 and price[i] >price[j]):
      S[i]+=1
      j-=1
  return S


































'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)