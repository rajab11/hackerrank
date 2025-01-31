"""
Task

The National University conducts an examination of  students in  subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 
Input Format

The first line contains  and  separated by a space.
The next  lines contains the space separated marks obtained by students in a particular subject.

Constraints



Output Format

Print the averages of all students on separate lines.

The averages must be correct up to  decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
Sample Output

90.0 
91.0 
82.0 
90.0 
85.5        
Explanation

Marks obtained by student 1: 
Average marks of student 1:

Marks obtained by student 2: 
Average marks of student 2:

Marks obtained by student 3: 
Average marks of student 3:

Marks obtained by student 4: 

"""
n,x=map(int,input().split()) #number of students and subjects

# Read all subject marks
marks = [list(map(float, input().split())) for _ in range(x)]

# Calculate the average for each student
averages = [sum(student) / x for student in zip(*marks)]

# Print the result with 1 decimal place
for avg in averages:
    print(f"{avg:.1f}")