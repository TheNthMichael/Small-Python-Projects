def lens(prev=lambda x: 0):
    """
    A lens store is a store that associates keys with values.
    
    To create a lens store, call the function 'lens', to get a 'put' function.
    This function enables you to "put" a key-value pair into the store, and
    returns two functions 'get' and another 'put'. The 'get' function should
    let you look up a key and return its corresponding value, while the 
    new 'put' function should let you continue adding on to the existing lens store.

    Note that you can assume that every key provided is unique. If you try to
    get the value for a key that does not exist, return 0.

    For details, refer to the doctest.

    >>> put1 = lens()
    >>> get2, put2 = put1('cat', 'animal')
    >>> get3, put3 = put2('table', 'furniture')
    >>> get4, put4 = put3('cup', 'utensil')
    >>> get5, put5 = put4('thesis', 'paper')
    >>> get5('thesis')
    'paper'
    >>> get5('cup')
    'utensil'
    >>> get5('table')
    'furniture'
    >>> get5('cat')
    'animal'
    >>> get3('cup')
    0
    """
    def put(k, v):
        def get(k2):
            if k2 == k:
                return v
            else:
                return prev(k2)
        return get, lens(get)
    return put


"""
Another set of problem using Sequences

"""
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)


"""
    min = minimum_perimeter(area)
    min = 2 * w + 2 * h: for a w & h that satisfy those conditions, we will have a minimum perimeter for a given area
"""

"""
Using Higher Order Functions with Sequence Processing
     Evaluating an expression for each element in a sequence 
     can be expressed by applying a function to each element.

"""
def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

"""
Many forms of aggregation can be expressed as repeatedly
 applying a two arg function to the reduced value so far 
 and each element in turn

"""
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def sum_of_divisors(n):
    return reduce(lambda x, y: x + y, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n


"""
Trees

"""
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

""" Binarization 
    finds a binarized tree with the same labels as an original tree
    by grouping together brancjhes
"""
def right_binarize(t):
    """Construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))

def binarize_branches(bs):
    """Binarize a list of branches."""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [right_binarize(first), binarize_branches(rest)]
    else:
        return [right_binarize(b) for b in bs]

"""
Linked Lists
    sequence constructed from nested pairs
"""
def is_link(s):
    """S is a linked list if it is empty or a (first, rest) pair."""
    return s == 'empty' or (len(s) == 2 and is_link(s[1]))
    
def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != 'empty', "empty linked list has no first element"
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != 'empty', "empty linked list has no rest."
    return s[1]

def len_link(s):
    """Returns the length of a linked list."""
    count = 0
    while s != 'empty':
        s, count = rest(s), count + 1
    return count

def getitem(s, i):
    """Return the ith item from a linked list."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)
 
def len_link_recursive(s):
    """Recursively computes the length of a linked list."""
    if s == 'empty':
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i-1)

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    if s == 'empty':
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def apply_to_all_links(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == 'empty':
        return s
    else:
        return link(f(first(s)), apply_to_all_links(f, rest(s)))

def keep_if_links(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == 'empty':
        return s
    else:
        kept = keep_if_links(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

def join_links(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == 'empty':
        return ""
    elif rest(s) == 'empty':
        return str(first(s))
    else:
        return str(first(s)) + separator + join_links(rest(s), separator)
    
def partitions_link(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked List.
    """
    if n == 0:
        return link('empty', 'empty') # a list containing the empty partition
    elif n < 0 or m == 0:
        return 'empty'
    else:
        using_m = partitions_link(n-m, m)
        with_m = apply_to_all_links(lambda s: link(m, s), using_m)
        without_m = partitions_link(n, m-1)
        return extend_link(with_m, without_m)

def print_partition_link(n, m):
    lists = partitions_link(n,m)
    strings = apply_to_all_links(lambda s: join_links(s, " + "), lists)
    print(join_links(strings, "\n"))
    


"""  
Maximum subnumber
    Shows how we can enumerate all possible answers and pick the best one using tree recursion

"""
def sculptural(ruler, k):
    """
    Given a number 'ruler', find the largest number of length 'k' or fewer,
    composed of digits from 'ruler', in order.

    >>> sculptural(1234, 1)
    4
    >>> sculptural(32749, 2)
    79
    >>> sculptural(1917, 2)
    97
    >>> sculptural(32749, 18)
    32749
    """
    if k == 0 or ruler == 0:
        return 0
    a = (ruler % 10) + sculptural(ruler // 10, k - 1) * 10
    b = sculptural(ruler // 10, k)
    return max(a, b)


