"""
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°
"""
import math
ab=int(input())
bc=int(input())
if ab==bc:
    angle_mbc_degree=45
else:
    ac=math.sqrt(ab**2+bc**2)
    cos_mbc=bc/ac    
    cos_mbc=max(-1,min(1,cos_mbc))
    angle_mbc_radians=math.acos(cos_mbc)
    angle_mbc_degree=math.degrees(angle_mbc_radians)

print(f"{int(round(angle_mbc_degree))}\u00b0")