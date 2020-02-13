# Ben Dreyer
# Quicksort
# 2.9.2020
# This sorting algorithm sorts a data set based on a pivot, time complexity: O(nlogn) for best case, O(n^2) worst case

from random import randint

# Create a random array
def create_array(size=10, max=50):
    return [randint(0, max) for _ in range(size)]

def quicksort(data):
    if len(data) <= 1:        # Any array/list of length 0 or 1 is already sorted
        return data
    smaller, equal, larger = [], [], []
    pivot = data[randint(0, len(data) - 1)]

    for x in data:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            larger.append(x)
    return quicksort(smaller) + equal + quicksort(larger)


hack = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print hack
s = quicksort(hack)
print s
# Uncomment code below to test quicksort
# u = create_array()
# print "Unsorted: ", u
# s = quicksort(u)
# print "Sorted: ", s