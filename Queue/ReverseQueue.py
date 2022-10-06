from sys import stdin, setrecursionlimit
import queue


def reverseQueue(inputQueue) :
  if inputQueue.qsize() == 1:
    return inputQueue
  data = inputQueue.get()
  reverseQueue(inputQueue)
  inputQueue.put(data)
  return
def reverseKElements(inputQueue, k) :
  reverseQueue2(inputQueue,k)
  l = inputQueue.qsize()
  x = l - k
  while(x != 0):
    data = inputQueue.get()
    inputQueue.put(data)
    x-=1
  return




def reverseQueue2(inputQueue,k):
  if k == 0:
    return
  data = inputQueue.get()
  reverseQueue2(inputQueue,k-1)
  inputQueue.put(data)
  return
inputQueue = queue.Queue()
reverseQueue(inputQueue)