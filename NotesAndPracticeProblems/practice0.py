"""
Iterators are objects that allow us to go through the elements in a container in some order

s = [1,2,3]
t = iter(s)
next(s)
next(s)


An iterable value is any value taht can be passed to iter to produce an iterator
an iterator is returned from iter and can be passed to next; all iterators are mutable
A dictionary, its keys, its values, and its items are all iterable values
    -   The order of items in a dictionary is the order in which they were added (3.6)
    -   Historically, items appeared in an arbitrary order(<=3.5)

d = { 'one': 1, 'two': 2, 'three':3 }
d['zero'] = 0
k = iter(d.keys())

next(k) -> return keys

k = iter(d.values())
next(k) -> return values

You cannot change the size of the container while using an iterator else it will raise an exception

map(func, container)
    returns an iterator that calls func on each ``next(iter)``
"""

def double(x):
    print(' -- ', x, ' => ', 2*x, ' -- ')
    return 2*x

def notmain(s):
    m = map(double, s)
    f = lambda y: y >= 10
    t = filter(f, m)
    return list(t)



""" Generators and Generator Functions
    A generator function is a function that yields values instead of returning them
    A normal function returns once; a generator function can yield multiple times
    A generator is an iterator created automatically by calling a generator function
    When a generator function is called, it retrns a generator that iterates over its yields

"""

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


""" Generators can yield from iterators
A yield from statement yields all values from an iterator or iterable (3.3)

"""

def a_then_b(a, b):
    yield from a
    yield from b

def a_then_b_equiv(a,b):
    for x in a:
        yield x
    for x in b:
        yield x

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'end'

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])




def countSubstrings(s, queries):
    #
    # Write your code here.
    #
    for q in queries:
        sub = s[q[0]:q[1]+1]
        seq = set(substrings(sub))
        print(len(seq))
        m = set([x for x in '!@#$%^&*()-+'])
        'a'.isdig


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    """
    Its length is at least 6.
    It contains at least one digit. a
    It contains at least one lowercase English character. b 
    It contains at least one uppercase English character. c
    It contains at least one special character. The special characters are: !@#$%^&*()-+ d
    """
    # Return the minimum number of characters to make the password strong
    num_needed = 4

    s = [False, False, False, False]
    m = set([x for x in '!@#$%^&*()-+'])
    for c in password:
        if m.__contains__(c) and s[3] == False:
            s[3] = True
            num_needed -= 1
        elif c.isupper() and s[2] == False:
            s[2] = True
            num_needed -= 1
        elif c.islower() and s[1] == False:
            s[1] = True
            num_needed -= 1
        elif c.isdigit() and s[0] == False:
            s[0] = True
            num_needed -= 1

    extra = 6 - (num_needed + n)
    if extra >= 0:
        return num_needed + extra
    return num_needed

# Converts a given number < 60 into its english name
def num2Text(m):
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty', 'fourty', 'fifty']
    pre = ""
    # logic a
    if m == 15 or m == 45:
        pre = "quarter"
    elif m == 30:
        pre = "half"
    elif m >= 11 and m <= 19:
        pre = teens[m % 10]
    elif m <= 9:
        pre = units[m]
    elif m % 10 == 0:
        pre = tens[m // 10]
    else:
        pre = tens[m // 10] + " " + units[m % 10]
    return pre


    # Complete the timeInWords function below.
def timeInWords(h, m):
    suf = ""
    # logic c
    if m == 0:
        return num2Text(h) + " o' clock"
    elif m <= 30:
        if m != 15 and m != 30:
            suf += " minute"
            if m != 1:
                suf += "s"
        suf += " past "
        return num2Text(m) + suf + num2Text(h)
    else:
        m = 60 - m
        h = h + 1
        if m != 15 and m != 30:
            suf += " minute"
            if m != 1:
                suf += "s"
        suf += " to "
        return num2Text(m) + suf + num2Text(h)


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    n = len(c)
    people = [0 for _ in range(k)]
    person = 0
    c.sort()
    rev = reversed(c)

    cost = 0

    for i in rev:
        people[person] += 1
        cost += people[person] * i
        person = (person + 1) % k # go through each person reversed order- assume sorted
        
    return cost
        