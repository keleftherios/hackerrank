"""
https://www.hackerrank.com/challenges/absolute-permutation/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
Difficulty: MEDIUM

We define P to be a permutation of the first n natural numbers in the range [1, n] .
Let pos[i] denote the value at position i in permutation P using 1-based index.

P is considered to be an absolute permutation if |pos[i] - i| = k holds true for every i E [1, n].

Given n and k, print the lexicographically smallest absolute permutation P.
If no absolute permutation exists, print -1.

Example:
n = 4
k = 2

Create an array of elements from 1 to n, pos = [1, 2, 3, 4].
Using 1 based indexing, create a permutation where every |pos[i] - i| = k.
It can be rearranged to [3, 4, 1, 2] so that all of the absolute differences equal k = 2:

pos[i]      i       |pos[i] - i|
  3         1             2
  4         2             2
  1         3             2
  2         4             2

Function Description:
Complete the absolutePermutation function in the editor below.

absolutePermutation has the following parameter(s):
- int n: the upper bound of natural numbers to consider, inclusive
- int k: the absolute difference between each element's value and its index

Return:
- int[n]: the lexicographically smallest permutation, or [-1] if there is none.

Input Format:
The first line contains an integer t, the number of queries.
Each of the next t lines contains 2 space-separated integers, n and k.

Constraints:
- 1 <= t <= 10
- 1 <= n <= 10^5
- 0 <= k <= n

Sample Input:
STDIN   Function
-----   --------
3       t = 3 (number of queries)
2 1     n = 2, k = 1
3 0     n = 3, k = 0
3 2     n = 3, k = 2

Sample Output:
2 1
1 2 3
-1

Explanation:

Test_Case_0:
Position            :       1       2
Permutation         :       2       1
Absolute Difference :       1       1

Test_Case_1:
Position            :       1       2       3
Permutation         :       1       2       3
Absolute Difference :       0       0       0

Test_Case_2:
No absolute permutation exists, so we print -1 on a new line.

-----------------------------------------------------------------------------------------------------------------------
SOLUTION:
The task can only be solved under the condition that the array is divided into blocks of size multiples of 2*k,
where in each block, result[i] = input[i] + k for "k" times and result[i] = input[i] - k for "k" times.

For example, for k=2, (k+1, k+2, 3-k, 4-k) (k+5, k+6, 7-k, 8-k) ... result=[3,4,1,2, 7,8,5,6, ...]
"""


import math
import os
import random
import re
import sys
from numpy.f2py.crackfortran import traverse


#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

# def shift_list(alist: list) -> list:
#     pop_item = alist.pop()
#     alist.insert(0, pop_item)
#     return alist


def absolutePermutation(n: int, k: int) -> list:
    """
    The task can only be solved under the condition that the array
    is divided into blocks of size multiples of 2*k, where in each block,
    result[i] = input[i] + k for "k" times and
    result[i] = input[i] - k for "k" times.

    For example:
    for k = 2, (k+1, k+2, 3-k, 4-k) (k+5, k+6, 7-k, 8-k) ...
    result = [3,4,1,2, 7,8,5,6, ...]
    """

    if k == 0:
        return [i for i in range(1, n + 1)]

    if (n / k) % 2 != 0:
        return [-1]

    alist = []
    bool_flag = True
    for i in range(n // k):
        for j in range(k):
            res = i * k + 1 + j + (k if bool_flag else -k)
            alist.append(res)
        bool_flag = not bool_flag
    return alist


def test_absolute_permutation(n, k, expected_result):
    print(f"n = {n} \nk = {k}")
    result = absolutePermutation(n, k)
    assert (result == expected_result), f"{result} vs {expected_result}"
    print(f"result = {result}\n")


if __name__ == '__main__':

    # Test_1:
    exp_res1 = [3, 4, 1, 2]
    test1 = (4, 2, exp_res1)
    result1 = test_absolute_permutation (*test1)

    # Test_2:
    exp_res2 = [2, 1]
    test2 = (2, 1, exp_res2)
    result2 = test_absolute_permutation(*test2)

    # Test_3:
    expr_res3 = [1, 2, 3]
    test3 = (3, 0, expr_res3)
    result3 = test_absolute_permutation(*test3)

    # Test_4:
    exp_res4 = [-1]
    test4 = (3, 2, exp_res4)
    result4 = test_absolute_permutation(*test4)

    # Test_5:
    exp_res5 = [3, 4, 1, 2, 7, 8, 5, 6]
    test5 = (8, 2, exp_res5)
    result5 = test_absolute_permutation(*test5)

    # Test_5:
    exp_res6 = [3, 4, 1, 2, 7, 8, 5, 6, 11, 12, 9, 10]
    test6 = (12, 2, exp_res6)
    result6 = test_absolute_permutation(*test6)

    # Test_7:
    exp_res7 = [3, 4, 1, 2, 7, 8, 5, 6, 11, 12, 9, 10,
            15, 16, 13, 14, 19, 20, 17, 18, 23, 24,
            21, 22, 27, 28, 25, 26, 31, 32, 29, 30,
            35, 36, 33, 34, 39, 40, 37, 38, 43, 44,
            41, 42, 47, 48, 45, 46, 51, 52, 49, 50,
            55, 56, 53, 54, 59, 60, 57, 58, 63, 64,
            61, 62, 67, 68, 65, 66, 71, 72, 69, 70,
            75, 76, 73, 74, 79, 80, 77, 78, 83, 84,
            81, 82, 87, 88, 85, 86, 91, 92, 89, 90,
            95, 96, 93, 94, 99, 100, 97, 98]
    test7 = (100, 2, exp_res7)
    result7 = test_absolute_permutation(*test7)

    # Test_8:
    exp_res8 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    test8 = (60, 10, exp_res8)
    result8 = test_absolute_permutation(*test8)
