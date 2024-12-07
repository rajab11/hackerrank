from itertools import combinations

# Input
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
