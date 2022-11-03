s = "Hello I am Mriganka I am Very Much Passionate about Software"
l = s.split()
# print(l)


def KFrequency(l, k):
  a = {}
  for items in l:
    a[items] = a.get(items, 0) + 1

  for value in a:
    if a[value] == k:
      print(value)

KFrequency(l,2)