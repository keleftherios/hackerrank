"""
https://www.hackerrank.com/challenges/beautiful-triplets/problem
Difficulty: EASY

Given a sequence of integers , a triplet (a[i], a[j], a[k]) is beautiful if:
- i < j < k
- a[j] - a[i] = a[k] - a[j] = d
Given an increasing sequence of integers and the value of sequence.

Example:
arr = [0, 2, 3, 4, 5]
d = 1

There are three beautiful triplets, by index:
[i, j, k] = [0, 2, 3], [1, 2, 3], [2, 3, 4].
To test the first triplet:
arr[j] - arr[i] = 3 - 2 = 1
and
arr[k] - arr[j] = 4 - 3 = 1

Function Description:
Complete the beautifulTriplets function in the editor below.
beautifulTriplets has the following parameters:
- int d: the value to match
- int arr[n]: the sequence, sorted ascending

Returns:
- int: the number of beautiful triplets

Input Format:
The first line contains 2 space-separated integers, n and d, the length of the sequence and the beautiful difference.
The second line contains n space-separated integers arr[i].

Constraints:
- 1 <= n <= 10^4
- 1 <= d <= 20
- 0 <= arr[i] > arr[i - 1]

Sample Input:
STDIN           Function
-----           --------
7 3             arr[] size n = 7, d = 3
1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]

Sample Output:
3

Explanation:
There are many possible triplets (arr[i], arr[j], arr[k]),
but our only beautiful triplets are (1, 4, 7),(4, 7, 10) and (2, 5, 8) by value, not index.

Please see the equations below:
7 - 4 = 4 - 1 = 3 = d
10 - 7 = 7 - 4 = 3 = d
8 - 5 = 5 - 2 = 3 = d

Recall that a beautiful triplet satisfies the following equivalence relation:
arr[j] - arr[i] = arr[k] - arr[i] = d
where
i < j < k.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    count = 0
    for num in arr:
        if num + d in arr and num + d * 2 in arr:
            count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # d = int(first_multiple_input[1])
    #
    # arr = list(map(int, input().rstrip().split()))

    arr = [1, 2, 4, 5, 7, 8, 10]
    # arr = [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]
    d = 3
    # d = 1

    result = beautifulTriplets(d, arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()