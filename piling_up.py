"""
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example

Result: No

After choosing the rightmost element, , choose the leftmost element, . After than, the choices are  and . These are both larger than the top block of size .


Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints



Output Format

For each test case, output a single line containing either Yes or No.

Sample Input

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .

"""
from collections import deque

t=int(input()) #input of number of test cases

for _ in range(t):
    n=int(input()) #number of cubes
    blocks=deque(map(int,input().split())) #input the side lengths

    last_picked=float('inf') #starting with infiniary large blocks
    possible=True

    while blocks:
        if blocks[0]>=blocks[-1]:
            chosen=blocks.popleft()
        else:
            chosen=blocks.pop()
        
        if chosen>last_picked:
            possible=False
            break
        
        last_picked=chosen
    
    print("Yes" if possible else "No")
