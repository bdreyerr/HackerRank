# Ben Dreyer
# Recursive Binary Search
# 2.9.2020
# This function has time complexity O(logn) and performs a binary search for a target on a data set
def recursive_binary_search(data, target, low, high):
    if low > high:
        return False
    mid = (high + low) // 2  # Target is the midpoint, exit
    if mid == target:
        return True
    elif target < mid:  # Target is left of midpoint
        recursive_binary_search(data, target, low, mid - 1)
    elif target > mid:  # Target is right of midpoint
        recursive_binary_search(data, target, mid + 1, low)
