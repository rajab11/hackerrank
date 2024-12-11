"""
You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

Constraints



All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length  comprising of indices from  to  are:


Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.

Hence, the answer is 5/6.
"""
#Input
n = int(input())  # Length of the list
letters = input().split()  # List of letters
k = int(input())  # Number of indices to select

# Count occurrences of 'a'
m = letters.count('a')


# Calculate total combinations
from math import comb
total_combinations = comb(n, k)

# Calculate unfavorable combinations
unfavorable_combinations = comb(n - m, k) if n - m >= k else 0

# Calculate probability
probability = 1 - (unfavorable_combinations / total_combinations)

# Print the result rounded to 4 decimal places
print(f"{probability:.4f}")
