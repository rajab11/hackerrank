def can_stack_cubes(test_cases):
    results = []
    for blocks in test_cases:
        stack = []
        while blocks:
            if blocks[0] >= blocks[-1]:
                block = blocks.pop(0)  # Pick leftmost block
            else:
                block = blocks.pop()  # Pick rightmost block
            
            # Check if stack is valid
            if not stack or stack[-1] >= block:
                stack.append(block)
            else:
                results.append("No")
                break
        else:
            results.append("Yes")
    return results

# Input processing
T = int(input("Enter number of test cases: "))
test_cases = []
for _ in range(T):
    n = int(input("Enter number of cubes: "))  # Number of cubes (not used directly)
    blocks = list(map(int, input("Enter cube side lengths: ").split()))
    test_cases.append(blocks)

# Solve and print results
results = can_stack_cubes(test_cases)
for result in results:
    print(result)
