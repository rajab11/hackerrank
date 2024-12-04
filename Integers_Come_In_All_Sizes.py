"""
Read four numbers, , , , and , and print the result of .

Input Format
Integers , , , and  are given on four separate lines, respectively.

Constraints




Output Format
Print the result of  on one line.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232  
Note: This result is bigger than . Hence, it won't fit in the long long int of C++ or a 64-bit integer.
"""
a=int(input())
b=int(input())
c=int(input())
d=int(input())

print(pow(a,b)+pow(c,d))