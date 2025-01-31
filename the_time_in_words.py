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

    # Check if h is int or not
    if not isinstance(h, int):
        h = int(h)

    # Check if m is int or not
    if not isinstance(m, int):
        m = int(m)

    # Define clock_numbers dictionary
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

    # Define 'minutes' or 'minute' word
    word_for_minutes = 'minutes' if m != 1 else 'minute'

    # Variable definition according to 'm'
    # ('m' is always going to be in the range of 0 <= m <= 30)
    if m > 30:
        m = 60 - m
        h += 1
        relation = 'to'
    else:
        relation = 'past'

    # Define hours
    hours = clock_numbers[h]

    # Check in 'm' is in the dictionary 'clock_numbers' or not and define minutes
    if 20 < m < 30:
        minutes = f"{clock_numbers[20]} {clock_numbers[m % 20]}"
    else:
        minutes = clock_numbers[m]

    # (same as above block, but perhaps not so clear)
    # try:
    #     minutes = clock_numbers[m]
    # except KeyError:
    #     minutes = f"{clock_numbers[20]} {clock_numbers[m % 20]}"

    # Final logic
    if not m:
        time_in_words = f"{hours} {minutes}"
    else:
        if m in [15, 30]:
            time_in_words = f"{minutes} {relation} {hours}"
        else:
            time_in_words = f"{minutes} {word_for_minutes} {relation} {hours}"
    return time_in_words


def check_function_timeInWords(h, m, expected_time_in_words_string):
    """
    Function to easily check the results of timeInWords
    """
    result = timeInWords(h, m)
    hour_str = str(h)
    min_str = str(m) + str(m) if not m else str(m)
    print(f"{hour_str}:{min_str} = {result}")
    assert result == expected_time_in_words_string, f"result = {result} vs exp_result = {expected_time_in_words_string}"


if __name__ == '__main__':

    # Test_1:
    check_function_timeInWords(5, 47, "thirteen minutes to six")

    # Test_2:
    check_function_timeInWords(3, 00, "three o' clock")

    # Test_3:
    check_function_timeInWords(7, 15, "quarter past seven")

    # Test_4:
    check_function_timeInWords(5, 28, "twenty eight minutes past five")

    # Test_5
    check_function_timeInWords(5, 45, "quarter to six")

    # Test_6
    check_function_timeInWords(5, 30, "half past five")

    # Test_7:
    check_function_timeInWords(5, 29, "twenty nine minutes past five")

    # Test_8:
    check_function_timeInWords(5, 31, "twenty nine minutes to six")

    # Test_9
    check_function_timeInWords(5, 40, "twenty minutes to six")

    # Test_10
    check_function_timeInWords(5, 39, "twenty one minutes to six")

    # Test_11
    check_function_timeInWords(5, 41, "nineteen minutes to six")

    # Test_12:
    check_function_timeInWords(5, 20, "twenty minutes past five")

    # Test_13:
    check_function_timeInWords(5, 19, "nineteen minutes past five")

    # Test_14:
    check_function_timeInWords(5, 21, "twenty one minutes past five")

