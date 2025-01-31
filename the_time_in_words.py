"""
https://www.hackerrank.com/challenges/the-time-in-words/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
Difficulty: MEDIUM

                    Given the time in numerals we may convert it into words, as shown below:
                    5:00 --> five o' clock
                    5:01 --> one minute past five
                    5:10 --> ten minutes past five
                    5:15 --> quarter past five
                    5:30 --> half past five
                    5:40 --> twenty minutes to six
                    5:45 --> quarter to six
                    5:47 --> thirteen minutes to six
                    5:28 --> twenty eight minutes past five

- At minutes = 0, use "o' clock"
- For 1 <= minutes <= 30, use "past".
- For 30 < minutes use "to".

Note the space between the apostrophe and clock in "o' clock".
Write a program which prints the time in words for the input given in the format described.

Function Description:
Complete the timeInWords function in the editor below.
timeInWords has the following parameter(s):
- int h: the hour of the day
- int m: the minutes after the hour

Returns:
- string: a time string described.

Input Format:
The first line contains h, the hours position.
The second line contains m, the minutes position.

Constraints:
- 1 <= h <= 12
- 0 <= m < 60

Sample Input O:
thirteen minutes to six

Sample Input 1:
3
00

Sample Output 1:
three o' clock

Sample Input 2:
7
15

Sample Output 2:
quarter past seven
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h: int, m: int):
    """
    Solution for the time_in_words'
    """

    if not isinstance(h, int):
        h = int(h)

    if not isinstance(m, int):
        m = int(m)

    clock_numbers = {0: "o' clock",
                     1: "one",
                     2: "two",
                     3: "three",
                     4: "four",
                     5: "five",
                     6: "six",
                     7: "seven",
                     8: "eight",
                     9: "nine",
                     10: "ten",
                     11: "eleven",
                     12: "twelve",
                     13: "thirteen",
                     14: "fourteen",
                     15: "quarter",
                     16: "sixteen",
                     17: "seventeen",
                     18: "eighteen",
                     19: "nineteen",
                     20: "twenty",
                     30: "half"}

    word_for_minutes = 'minutes' if m != 1 else 'minute'

    if m > 30:
        m = 60 - m
        h += 1
        relation = 'to'
    else:
        relation = 'past'

    hours = clock_numbers[h]

    if 20 < m < 30:
        minutes = f"{clock_numbers[20]} {clock_numbers[m % 20]}"
    else:
        minutes = clock_numbers[m]

    if not m:
        time_in_words = f"{hours} {minutes}"
    else:
        if m in [15, 30]:
            time_in_words = f"{minutes} {relation} {hours}"
        else:
            time_in_words = f"{minutes} {word_for_minutes} {relation} {hours}"
    return time_in_words


if __name__ == '__main__':

    # Test_1:
    test1 = (5, 47)
    result1 = timeInWords(*test1)
    print(f"{test1[0]}:{test1[1]} = {result1}")
    assert result1 == "thirteen minutes to six", "Wrong answer for test1... "

    # Test_2:
    test2 = (3, 00)
    result2 = timeInWords(*test2)
    print(f"{test2[0]}:{test2[1]} = {result2}")
    assert result2 == "three o' clock", "Wrong answer for test2... "

    # Test_3:
    test3 = (7, 15)
    result3 = timeInWords(*test3)
    print(f"{test3[0]}:{test3[1]} = {result3}")
    assert result3 == "quarter past seven", "Wrong answer for test3... "

    # Test_4:
    test4 = (5, 28)
    result4 = timeInWords(*test4)
    print(f"{test4[0]}:{test4[1]} = {result4}")
    assert result4 == "twenty eight minutes past five", "Wrong answer for test4..."

    # Test_5
    test5 = (5, 45)
    result5 = timeInWords(*test5)
    print(f"{test5[0]}:{test5[1]} = {result5}")
    assert result5 == "quarter to six", "Wrong answer for test5..."

    # Test_6
    test6 = (5, 30)
    result6 = timeInWords(*test6)
    print(f"{test6[0]}:{test6[1]} = {result6}")
    assert result6 == "half past five", "Wrong answer for test6..."

    # Test_7
    test7 = (5, 40)
    result7 = timeInWords(*test7)
    print(f"{test7[0]}:{test7[1]} = {result7}")
    assert result7 == "twenty minutes to six", "Wrong answer for test7..."
