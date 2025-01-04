"""
Lisa just got a new math workbook.
A workbook contains exercise problems, grouped into chapters.
Lisa believes a problem to be special if:
-- its index (within a chapter) is the same as the page number where it's located.
The format of Lisa's book is as follows:

-- There are n chapters in Lisa's workbook, numbered from 1 to n.
-- The i-th chapter has arr[i] problems, numbered from 1 to arr[i].
-- Each page can hold up to k problems. Only a chapter's last page of exercises
   may contain fewer than problems k problems.
-- Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
-- The page number indexing starts at 1.

Given the details for Lisa's workbook, can you count its number of special problems?

Example:
arr = [4, 2]
k = 3

Lisa's workbook contains arr[1] = 4 problems for chapter 1, and arr[2] = 2 problems for chapter 2.
Each page can hold k = 3 problems.
The first page will hold 3 problems for chapter 1. Problem 1 is on page 1, so it is special.
Page 2 contains only Chapter 1, Problem 4, so no special problem is on page 2.
Chapter 2 problems start on page 3 and there are 2 problems. Since there is no problem 3 on page 3,
there is no special problem on that page either. There is 1 special problem in her workbook.

Note: See the diagram in the Explanation section for more details.

Function Description:
Complete the workbook function in the editor below.

workbook has the following parameter(s):

-- int n: the number of chapters
-- int k: the maximum number of problems per page
-- int arr[n]: the number of problems in each chapter

Returns
-- int: the number of special problems in the workbook

Input Format:
The first line contains two integers n and k, the number of chapters and the maximum number of problems per page.
The second line contains n space-separated integers arr[i],
where arr[i] denotes the number of problems in the i-th chapter.

Constraints:
1 <= n, k, arr[i] <= 100

Sample Input:
STDIN        Function
-----        --------
5 3          n = 5, k = 3
4 2 6 1 10   arr = [4, 2, 6, 1, 10]

Sample Output:
4

Explanation:
The diagram below depicts Lisa's workbook with n = 5 chapters and a maximum of k = 3 problems per page.
Special problems are outlined in star.

There are 4 special problems, and thus we print the number 4 on a new line.

 ____________    ____________    ____________    ____________    ____________
| Chapter: 1 |  | Chapter: 1 |  | Chapter: 2 |  | Chapter: 3 |  | Chapter: 3 |
|            |  |            |  |            |  |            |  |            |
| *1, 2, 3   |  | 4          |  | 1, 2       |  | 1, 2, 3    |  | 4, *5, 6   |
|            |  |            |  |            |  |            |  |            |
| Page: 1    |  | Page: 2    |  | Page: 3    |  | Page: 4    |  | Page: 5    |
| spec pr: 1 |  | spec pr:   |  | spec pr:   |  | spec pr:   |  | spec pr: 5 |
 ------------    ------------    ------------    ------------    ------------

 ____________    ____________    ____________    ____________    ____________
| Chapter: 4 |  | Chapter: 5 |  | Chapter: 5 |  | Chapter: 5 |  | Chapter: 5 |
|            |  |            |  |            |  |            |  |            |
| 1          |  | 1, 2, 3    |  | 4, 5, 6    |  | 7, 8, *9   |  | *10        |
|            |  |            |  |            |  |            |  |            |
| Page: 6    |  | Page: 7    |  | Page: 8    |  | Page: 9    |  | Page: 10   |
| spec pr:   |  | spec pr:   |  | spec pr:   |  | spec pr: 9 |  | spec pr: 10|
 ------------    ------------    ------------    ------------    ------------

"""


import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    """
    My solution on Lisa's workbook.
    """
    if len(arr) != n:
        return
    current_page = special_problems = 0
    for chapter in range(n):
        if arr[chapter] < k:
            current_page += 1
            if current_page in range(1, arr[chapter] + 1):
                special_problems += 1
        else:
            quotient, remainder = arr[chapter] // k, arr[chapter] % k
            for i in range(quotient):
                current_page += 1
                start = k * i + 1
                end = start + k
                if current_page in range(start, end):
                    special_problems += 1
            if remainder:
                current_page += 1
                # 'end' variable will always have a value!
                start, end = end, end + remainder

                if current_page in range(start, end):
                    special_problems += 1
    return special_problems


def work_book(n, k, arr):
    """
    Another solution on Lisa's workbook.
    """
    special_problems = 0
    current_page = 1

    for chapter in range(n):
        total_problems = arr[chapter]
        problem_number = 1

        while problem_number <= total_problems:
            # Calculate the last problem on the current page
            last_problem_on_page = min(problem_number + k - 1, total_problems)

            # Check if the current page contains a special problem
            if problem_number <= current_page <= last_problem_on_page:
                special_problems += 1

            # Move to the next page and update the problem number
            current_page += 1
            problem_number = last_problem_on_page + 1

    return special_problems


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # k = int(first_multiple_input[1])
    #
    # arr = list(map(int, input().rstrip().split()))

    n1 = 5
    k1 = 3
    arr1 = [4, 2, 6, 1, 10]
    my_result1 = workbook(n1, k1, arr1)
    print(my_result1)

    n2 = 10
    k2 = 5
    arr2 = [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]
    my_result2 = workbook(n2, k2, arr2)
    print(my_result2)

    assert my_result1 == 4, f"Wrong answer..."
    assert my_result2 == 8, f"Wrong answer..."

    n3 = 12
    k3 = 66
    arr3 = [40, 33, 93, 66, 31, 13, 1, 88, 94, 6, 12, 90]
    my_result3, result3 =  workbook(n3, k3, arr3), work_book(n3, k3, arr3)
    assert my_result3 == result3, f"{my_result3} != {result3}"

    n4 = 19
    k4 = 50
    arr4 = [35, 60, 24, 5, 79, 24, 89, 53, 74, 58, 62, 70, 54, 50, 39, 48, 63, 4, 2]
    my_result4, result4 =  workbook(n4, k4, arr4), work_book(n4, k4, arr4)
    assert my_result4 == result4, f"{my_result4} != {result4}"

    print("----------------------------------------------------------------------------------------------")

    for _ in range(100):
        n = random.randint(10, 20)
        k = random.randint(1, 100)
        arr = [random.randint(1, 100) for _ in range(n)]
        print(f"\nn: {n}\nk: {k}\narr: {arr}")
        R1, R2 = workbook(n, k, arr), work_book(n, k, arr)
        assert R1 == R2, f"R1 = {R1} -- R2 = {R2}"

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()