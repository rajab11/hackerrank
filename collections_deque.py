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
    