n,x=map(int,input().split()) #number of students and subjects

# Read all subject marks
marks = [list(map(float, input().split())) for _ in range(x)]

# Calculate the average for each student
averages = [sum(student) / x for student in zip(*marks)]

# Print the result with 1 decimal place
for avg in averages:
    print(f"{avg:.1f}")