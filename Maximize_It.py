from itertools import product

def maximize_modulo(k, M, lists):
    # Generate all possible combinations
    all_combinations = product(*lists)
    max_value = 0
    
    # Evaluate each combination
    for combination in all_combinations:
        # Calculate the value of S
        current_value = sum(x ** 2 for x in combination) % M
        max_value = max(max_value, current_value)
    
    return max_value

# Input
k, M = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(k)]

# Output
result = maximize_modulo(k, M, lists)
print(result)
