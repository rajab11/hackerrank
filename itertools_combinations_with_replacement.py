"""
You are given a string S.
Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the combinations with their replacements of string  on separate lines.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""
from itertools import combinations_with_replacement

s,k=input().split()

k=int(k)
s=sorted(s)

result=[''.join(comb) for comb in combinations_with_replacement(s,k)]
for r in result:
    print(r)