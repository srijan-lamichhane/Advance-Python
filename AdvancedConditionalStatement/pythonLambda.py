# In Python, an anonymous function means that a function is without a name. 
# As we already know that def keyword is used to define the normal functions 
# and the lambda keyword is used to create anonymous functions.

# syntax: lambda arguments: expression

# To find the square of numbers
#traditional method:

def square_trad(x):
    return x*x # we cannot mulptiply list with a list.

numbers = list(range(1,6))
squared_nums = [square_trad(x) for x in numbers]
print(squared_nums)

# Using lambda function

square_lambda = lambda x: x*x 

numbers = list(range(1,6))
squared_nums = [square_lambda(x) for x in numbers]
print(squared_nums)

# optimized
numbers = range(1,6)
print(list(map(lambda x: x * x, numbers))) # or directly pass range(1,6) instead of numbers


# to find numbers divisible by 2.
calc = lambda num: "EVEN NUMBER" if num % 2 == 0 else "ODD NUMBER"
print(calc(10))

string = 'whattheflop'
print(lambda string: string.upper())

# filter_nums(): Geeks   --> Geeks101

filter_nums = lambda s:  ''.join([ch for ch in s if not ch.isdigit()]) # isdigit() function.
print(filter_nums('Geeks101'))

filter_nums = lambda s:  ''.join([ch for ch in s if ch.isdigit()])
print(filter_nums('Geeks101'))

do_exclaim = lambda s: s[:-1] if s[-1] == '!' else s
print(do_exclaim('I am tired!'))

# do_exclaim(): I am tired! --> I am tired

do_exclaim = lambda s: s + '!'
print(do_exclaim('I am tired'))

s = 'I am tired!'
print(s[-1])

# find_sum(): 101 --> 2

find_sum = lambda s: sum([int(ch)  for ch in s if ch.isdigit()])
print(find_sum('5101'))

