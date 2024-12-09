from collections import Counter

# Input reading
number_of_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
number_of_customers = int(input())

# Create inventory counter
inventory = Counter(shoe_sizes)

# Initialize earnings
earnings = 0

# Process each customer
for _ in range(number_of_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:  # Check if the size is available
        earnings += price
        inventory[size] -= 1  # Reduce the count for that size

# Output total earnings
print(earnings)
