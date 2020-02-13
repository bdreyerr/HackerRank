# Ben Dreyer
# Iterative Binary Search
# 2.9.2020
# This function has time complexity O(logn) and performs a binary search for a target on a data set
def iterative_binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == target:
            return True
        elif target < data[mid]:
            high = mid -1
        elif target > data[mid]:
            low = mid + 1
    return False

