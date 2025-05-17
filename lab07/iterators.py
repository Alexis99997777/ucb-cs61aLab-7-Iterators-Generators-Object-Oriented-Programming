def naturals():
    i = 1
    while True:
        yield i 
        i +=1

#q1 scale
def scale(it, multiplier):
    for i in it:
        yield i * multiplier

    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"



#q2 hailstone

def hailstone(n):
    if n <= 0:
        return "PICK A POSITIVE INTEGER"
    print(n)
    while n != 1:
        yield from (n/2 if n % 2 == 0 else 3*n+1) 
    return 1
    """
for num in hailstone(10):
    print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"



