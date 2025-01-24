"""
Given an array of strings of digits, try to find the occurrence of a given pattern of digits.
In the grid and pattern arrays, each string represents a row in the grid.
For example, consider the following grid:

1234567890
09*876543*21
11*111111*11
11*111111*11
2222222222

The patterns array is:
876543
111111
111111

The pattern begins at the second row and the third column of the grid and continues in the following two rows.
The pattern is said to be present in the grid. The return value should be YES or NO,
depending on whether the pattern is found. In this case, return YES.

Function Description:
Complete the gridSearch function in the editor below.
It should return YES if the pattern exists in the grid, or NO otherwise.

gridSearch has the following parameter(s):

- string G[R]: the grid to search
- string P[r]: the pattern to search for

Input Format:
The first line contains an integer t, the number of test cases.
Each of the t test cases is represented as follows:
The first line contains two space-separated integers R and C,
the number of rows in the search grid G and the length of each row string.

This is followed by R lines, each with a string of C digits that represent the grid G.

The following line contains two space-separated integers, r and c,
the number of rows in the pattern grid P and the length of each pattern row string.

This is followed by r lines, each with a string of c digits that represent the pattern grid P.

Returns:
- string: either YES or NO.

Constraints:
1 <= t <= 5
1 <= R,r,C,c <= 1000
1 <= r <= R
1 <=c <= C

Sample Input:
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99

Sample Output:
YES
NO

Explanation:

The first test in the input file is:
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530

The second test in the input file is:
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99

The search pattern is:
99
99

This pattern is not found in the larger grid.
"""



import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#


def gridSearch(G, P):

    R, C = len(G), len(G[0])
    r, c = len(P), len(P[0])

    indexes = []

    for grow in range(R - r + 1):
        grid = G[grow]

        for gcol in range(C - c + 1):
            grid_search = grid[gcol:gcol + c]

            if len(grid_search) < c:
                continue

            if grid_search == P[0]:
                grid_index, grid_row = gcol, grow
                indexes.append((grid_row, grid_index))

    if indexes:
        # print(f"INDEXES: {indexes}")
        count = 1
        for pattern in P[1:]:
            for grid_row, grid_index in indexes:
                for grow in range(grid_row + 1, grid_row + r):
                    grid_search = G[grow][grid_index:grid_index + c]
                    if pattern == grid_search:
                            count += 1
                    if count == r:
                        return "YES"
    return "NO"


if __name__ == '__main__':

    # Expected result: YES
    G1 = ["7283455864", "6731158619", "8988242643",
          "3830589324", "2229505813", "5633845374",
          "6473530293", "7053106601", "0834282956",
          "4607924137"]
    P1 = ["9505", "3845", "3530"]

    # Expected result: NO
    G2 = ["400453592126560", "114213133098692", "474386082879648",
          "522356951189169", "887109450487496", "252802633388782",
          "502771484966748", "075975207693780", "511799789562806",
          "404007454272504", "549043809916080", "962410809534811",
          "445893523733475", "768705303214174", "650629270887160"]
    P2 = ["99", "99"]

    # Expected result: NO (!!!)
    # This is because the pattern "12" starts at index "0", where pattern "21" starts at index "2".
    # In order to be a "YES", the two indexes should match (0 != 2)!!! E.g. grid = ["1234", "2134", "9999", "9999"]
    G3 = ["1234", "4321", "9999", "9999"]
    P3 = ["12", "21"]

    # Expected result: YES
    # This is because pattern "12" is found at two places in 1st grid row: at index "0-1" and at index "4-5"
    G4 = ["123412", "561212", "123634", "781288"]
    P4 = ["12", "12"]

    G5 = ["123412", "561212", "123634", "781288"]
    P5 = ["12", "36"]

    result1 = gridSearch(G1, P1)
    result2 = gridSearch(G2, P2)
    result3 = gridSearch(G3, P3)
    result4 = gridSearch(G4, P4)
    result5 = gridSearch(G5, P5)

    assert result1 == "YES", "Wrong answer for test1..."
    assert result2 == "NO", "Wrong answer for test2..."
    assert result3 == "NO", "Wrong answer for test3..."
    assert result4 == "YES", "Wrong answer for test4..."
    assert result5 == "YES", "Wrong answer for test5..."

    data = []
    input_file = "test5_the_grid_search.txt"
    with open(input_file, "r") as f:
        for line in f:
            data.append(line.rstrip())

    number_of_tests = data[0]

    C = R = c = r = 0
    start, end  = 1, 0
    for test, expected_result in enumerate(["YES", "YES", "NO", "YES", "NO"], start=1):
        print(f"TEST: {test}")
        C, R = data[start].split()
        print(f"C: {C} --- R: {R}")
        start += 1
        end = start + int(C)
        print(f"G[{start}:{end}]")
        G = data[start:end]
        start = end
        c, r = data[start].split()
        print(f"c: {c} --- r: {r}")
        start += 1
        end = start + int(c)
        print(f"P[{start}:{end}]")
        P = data[start:end]
        result = gridSearch(G, P)
        print(f"result = {result} --- Expected Result = {expected_result}")
        start = end
        end = start
        print()

        assert result == expected_result, f"Wrong answer for test: {test}"

    grid = data[3762:4762]
    pattern = data[4763:4767]



