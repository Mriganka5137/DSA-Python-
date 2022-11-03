a = {}
print(type(a))

b = {"a":1, "b":2, "c":3}
print(b)
print(len(b))

c = dict([("hello",5137),("world", 5137) ])
print(c)

d = dict.fromkeys(["a","b","c"])
print(d)

e = dict.fromkeys(["a","b","c"], 25)
print(e)


# Accessing Values and Keys of Dictionaries
# 1. Method 1
value = b["a"]
print(value)

# value = b["hello"]
# print(value)    Throws ERROR because there is no key as "hello"

value = b.get("a")
print(value)

value = b.get("Hello")   # Accessing keys which are not present with get function
print(value)

value = b.get("hello" , "I am not Present Buddy") # if any value is not present, it can be replaced with a default value which is passed with the function
print(value) 


result = b.keys()  # Gets all the keys of a dictionary
print(result)

print(b.values())  # Gets all the values of a dictionary

print(b.items())  # Gets all the key Value pairs


# Iterating through Dictionaries

for items in b.keys():
  print(items,":", b[items])

for items in b:   #Iterates only through the Keys
  print(items)


print(len(b))
