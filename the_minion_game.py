"""
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=false
Difficulty: MEDIUM

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

           STUARD                                    KEVIN
    WORDS           SCORE           |       WORDS           SCORE
      B               1             |         A               3
      N               2             |         AN              2
      BA              1             |        ANA              2
     BAN              1             |       ANAN              1
     NAN              1             |       ANANA             1
    BANA              1             |
    NANA              1             |
    BANAN             1             |
   BANANA             1             |
                                    |
TOTAL:               12             | TOTAL:                  9

Your task is to determine the winner of the game and their score.

Function Description:
Complete the minion_game in the editor below.
minion_game has the following parameters:
- string: the string to analyze.

Prints:
- string: the winner's name and score, separated by a space on one line, or Draw if there is no winner.

Input Format:
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A - Z].

Constraints:
0 < len(S) <= 10^6

Sample Input:
BANANA

Sample Output:
Stuard 12

NOTE:
Vowels are only defined as "AEIOU". In this problem, "Y" is NOT considered a vowel!
"""

import random
import string
import time

def minion_game_v1(string):
    """
    My first solution of 'The Minion Game'
    Even though this function is working, the solution is not efficient...
    The bigger the length of the word, the less efficient this function becomes.
    That's because of the nested for loops, which has an O(n^2) runtime.
    """
    vowels = "AEIOU"
    word_len = len(string)
    stuart_score = kevin_score = 0

    for j in range(1, word_len + 1):
        for i in range(word_len):
            word = string[i:i+j]
            if len(word) != j:
                continue
            if word[0] in vowels:
                kevin_score += 1
            else:
                stuart_score += 1

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


def minion_game(string):
    """
    Instead of generating all possible substrings,
    we count the number of substrings that start with
    a vowel or consonant.
    Considering a character at position i in the string,
    the number of substrings that start at i is equal to len(string) - i.
    This algorithm is much faster and efficient, since it calculates directly the score
    by avoiding generating the substrings. Runtime: O(n).
    """
    vowels = "AEIOU"
    word_len = len(string)
    stuart_score = kevin_score = 0
    score = None

    for i in range(word_len):
        if string[i] in vowels:
            kevin_score += word_len - i
        else:
            stuart_score += word_len - i

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    # s = input()

    alphabet = string.ascii_uppercase

    random_words = []
    rword = ''

    for _ in range(10):
        for _ in range(random.randint(1, 1000)):
            rword += alphabet[random.randint(1, 25)]
        random_words.append(rword)

    # print(random_words)

    for test in ["BANANA", "ANNA"]:
        minion_game_v1(test)
        minion_game(test)

    for s in random_words:
        t1 = time.time()
        minion_game_v1(s)
        t2 = time.time()

        t3 = time.time()
        minion_game(s)
        t4 = time.time()

        print(f"Function: {minion_game_v1.__name__} completed in {t2 - t1} sec!")
        print(f"Function: {minion_game.__name__}    completed in {t4 - t3} sec!")
        print()

