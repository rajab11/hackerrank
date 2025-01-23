"""
You are given a string S.
Your task is to find out whether s is a valid regex or not.

Input Format

The first line contains integer , the number of test cases.
The next  lines contains the string .

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
"""
import re
t=int(input()) #number of test cases

for _ in range(t):
    s=input().strip()
    try:
        re.compile(s)
        print("True")
    except re.error:
        print("False")
