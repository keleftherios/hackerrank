"""
https://www.hackerrank.com/challenges/counting-valleys/problem
Difficulty: EASY

An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly 'steps' steps,
for every step it was noted if it was an uphill, U, or a downhill, D step.
Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude.
We define the following terms:

- A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level
and ending with a step down to sea level.
- A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level
and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example:
steps = 8 path = [D D U U U U D D]
The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high.
Finally, the hiker returns to sea level and ends the hike.

Function Description:
Complete the countingValleys function in the editor below.
countingValleys has the following parameter(s):
- int steps: the number of steps on the hike
- string path: a string describing the path

Returns:
- int: the number of valleys traversed

Input Format:
The first line contains an integer steps, the number of steps in the hike.
The second line contains a single string path, of steps characters that describe the path.

Constraints:
- 2 <= steps 10^6
- path[i] E {UD}

Sample Input:
8
U D D D U D U U

Sample Output:
1

Explanation:
If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

_/\      _
   \    /
    \/\/

The hiker enters and leaves one valley.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    """
    Function that counts the valleys traversed
    """
    sea_level = valley = 0
    below_sea_level = False

    for i in range(steps):
        if path[i] == 'D':
            sea_level -= 1

        if path[i] == 'U':
            sea_level += 1

        if sea_level < 0 and not below_sea_level:
            below_sea_level = True

        if sea_level >= 0 and below_sea_level:
            below_sea_level = False
            valley += 1

    return valley


if __name__ == '__main__':

    # Test1
    steps1 = 8
    path1 = 'UDDDUDUU'
    test1 = (steps1, path1)

    # Test2
    steps2 = 8
    path2 = 'DDUUUUDD'
    test2 = (steps2, path2)

    # Test3
    steps3 = 12
    path3 = 'DDUUDDUDUUUD'
    test3 = (steps3, path3)

    expected_result = [1, 1, 2]

    for index, data in enumerate([test1, test2, test3]):
        result = countingValleys(*data)
        print(f"Test_{index+1}: result = {result} vs expected_result = {expected_result[index]}")
        assert result == expected_result[index], f"Wrong output for test_{index+1}..."

