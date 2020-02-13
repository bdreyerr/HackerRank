# Ben Dreyer
# Hacker Rank Interview Prep Warm up Challenges
# Sock Merchant
# 2.11.2020


# Constraint One: 1 <= n <= 100
# Constraint Two: Each element in ar 1 <= ar[i] <= 100
# Must make sure these constraints are true, otherwise return False

import math
import os
import random
import re
import sys

# Dont actually need to worry about the constraints, hacker rank pre made code takes care of it for you


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    ar.sort()
    ar.append(
        '!')  # This is just some random symbol used to mark the end of the array so that the last value of the list has something to compare itself too, obviously the last sock will not have a match if all the previous socks have either found a match or not and the list is sorted
    i = 0
    while i < n:
        if ar[i] == ar[i + 1]:
            pairs = pairs + 1
            i += 2
        else:
            i += 1
    return pairs


# Time complexity of sockMerchant is O(n) where n is the size of ar
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())  # First line input of the number of socks

    ar = map(int, raw_input().rstrip().split())  # Second line

    result = sockMerchant(n, ar)  # Function call to sockMerchant defined above

    fptr.write(str(result) + '\n')

    fptr.close()
