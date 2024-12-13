import sys
import statistics

input()  # Skip the number of students line
columns = input().split()  # Read and split the column names
marks_idx = columns.index("MARKS")  # Find the index of the "MARKS" column
print(f"{statistics.mean(int(input().split()[marks_idx]) for _ in range(int(sys.stdin.read().splitlines()[0]))):.2f}")
