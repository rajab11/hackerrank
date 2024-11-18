"""
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string  and the integer value .

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string  on separate lines.

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation

All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.
"""
from itertools import permutations

string=input()
s=[char for char in string.split()[0]]
k=int(string.split()[1])
result=sorted(list(permutations(s,k)))

for k in result:
    result=''.join(k)
    print(result)