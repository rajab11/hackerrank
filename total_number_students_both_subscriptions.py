"""
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format

The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Constraints


Output Format

Output the total number of students who have subscriptions to both English and French newspapers.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

5
Explanation

The roll numbers of students who have both subscriptions:
 1,2,3,6 and 8 .
Hence, the total is  students.
"""
# Input number of students and their roll numbers for English newspaper
n_english = int(input())
english_set = set(map(int, input().split()))

# Input number of students and their roll numbers for French newspaper
n_french = int(input())
french_set = set(map(int, input().split()))

# Find the intersection of both sets
both_subscriptions = english_set & french_set

# Output the number of students with both subscriptions
print(len(both_subscriptions))
