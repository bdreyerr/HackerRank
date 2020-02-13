# Ben Dreyer
# Mergesort
# 2.9.2020
# This algorithm splits an array in half until individuality is achieved, and merges items together in sorted order
# Time complexity is O(nlogn) in all cases

from random import randint

# Create a random array
def create_array(size=10, max=50):
    return [randint(0, max) for _ in range(size)]

# The merge function merges two sorted arrays / lists
def merge(a, b):
    c = []          # The final array
    x, y = 0, 0     # Index x for array a, Index y for array b
    while x < len(a) and y < len(b):        # This while loop appends values in sorted order
        if a[x] < b[y]:
            c.append(a[x])
            x += 1
        else:
            c.append(b[y])
            b += 1
    if x == len(a):
        c.extend(b[y:])
    else:
        c.extend(a[x:])
    return c

# The function that actually sorts the merged arrays, includes recursion
def merge_sort(a):
    if len(a) <= 1:     # An array of length 0 or 1 is already sorted
        return a
    left, right = merge_sort(a[:len(a)/2]), merge_sort(a[len(a)/2:])
    return merge(left, right)

a = create_array()
print a
s = merge_sort(a)
print s