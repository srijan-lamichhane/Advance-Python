# A dictionary comprehension takes the form {key: value for (key, value) in iterable}
# iterating with the help of zip() function.

myDict = dict([('a', 1), ('b', 2)])
print(myDict)

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
myDict = {k:v for (k,v) in zip(keys, values)}
print(myDict)

# traditional way of doing it. (without dictionary comprehension)
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

myDict = {}
for k,v in zip(keys, values):
    myDict[k] = v

print(myDict)

#  fromkeys() method:  returns a dictionary with specific keys and values.

dic = dict.fromkeys(range(5), True)
print(dic) 

keys = ['a','b','c','d','e']
myDict = dict(zip(range(5), keys))
print(myDict)

# dictionary comprehension using list comprehension.
# example 1:
res = {x: x**2 for x in [1,2,3,4,5]}
print(res)
# example 2:
res = {x.upper(): x*3 for x in 'coding'}
print(res)


# conditional statement in dictionary comprehension.
# example 1: maps the numbers to their cubes that are divisible by 4.

res = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(res)

# nested directory comprehension.
# find all combinations of the given word.

word = 'SRIJAN'

res = {
    i: {j: i + j for j in word} for i in word
}
print(res)