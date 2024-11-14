"""
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12
"""
# Step 1: Read inputs
m = int(input().strip())  # Read the number of elements in the first set
set_m = set(map(int, input().strip().split()))  # Read elements and convert to set

n = int(input().strip())  # Read the number of elements in the second set
set_n = set(map(int, input().strip().split()))  # Read elements and convert to set

# Step 2: Find the symmetric difference and sort the result
symmetric_diff = sorted(set_m.symmetric_difference(set_n))

# Step 3: Output each element on a new line
for num in symmetric_diff:
    print(num)
