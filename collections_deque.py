"""
Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2

"""
from collections import deque

#input
n=int(input())

d=deque()
for _ in range(n):
    inputs=list(input().split())
    oper=inputs[0]
    if oper=='pop':
        d.pop()
    if oper=='popleft':
        d.popleft()
    if oper=='append':
        d.append(inputs[1])
    if oper=='appendleft':
        d.appendleft(inputs[1])  

print(' '.join(d))
    