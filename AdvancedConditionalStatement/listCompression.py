#1. list comprehension: concise way to create lists.
# look at : range(), append() 

a = [2,3,4,5]
# for x in a:
#     print(x)
# res = [] # empty list

for x in a:
    res.append(x ** 2)  # square of a   
print (res)

# we can do this without using loop and initializing empty list using list comprehension
res = [x ** 2 for x in a]
print(res)

# conditional statement(if else) in list comprehension.

list1 = [2,3,4,5]

listcomp = [x ** 2 for x in list1 if x % 2 == 0] # for x in list1 if x % 2 == 0 returns 2 and 4.
print(listcomp)

# creating a list of numbers from 0 to 9 using range (eg of list compression)

print(range(10)) # it will print the range object itself but not the range.
# so first we need to convert the range object to list or iterate over it.
print(list(range(10)))

for i in range(10): # i will be an integer.
    print(list(i)) #Throws error: we cannot convert integer to list directly.

a = [i for i in range(10)]
print(a)

# generate a list of coordinate pairs for a simple 3×3 grid. (using nested loop in list comprehension)

coordinates = [(x,y) for x in range(3) for y in range(3)]
print(coordinates)

# traditional way of doing it. (without list comprehension)
coordinates = []
for x in range(3):
    for y in range(3):
        coordinates.append((x,y))

print(coordinates)


# flatten a list of lists using list comprehension.

list2 = [[1,2,3],[4,5,6],[7,8,9]] # I have to combine this to make one list.

flatten = [val for row in list2 for val in row]
print(flatten)

# traditional way of doing it. (without list comprehension)
list2 = [[1,2,3],[4,5,6],[7,8,9]]
flatten = []
for row in list2:
    for val in row:
        flatten.append(val)

print(flatten)

#revert process. (convert a flat list to list of lists)

flatten = [1,2,3,4,5,6,7,8,9]
list2 = [flatten[i:i+3] for i in range(0, len(flatten), 3)]
print(list2)


# traditional way of doing it. (without list comprehension)
flatten = [1,2,3,4,5,6,7,8,9]
list2 = []

for i in range(0, len(flatten), 3): # 0, 3, 6
    sublist = flatten[i:i+3] # 0:3, 3:6, 6:9
    # print(sublist)
    list2.append(sublist) # [[1,2,3],[4,5,6],[7,8,9]]

print(list2)