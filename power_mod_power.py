"""
You are given three integers: , , and . Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains , the second line contains , and the third line contains .

Constraints



Sample Input

3
4
5
Sample Output

81
1
"""

a=int(input())
b=int(input())
c=int(input())

print(pow(a,b))
print(pow(a,b,c))