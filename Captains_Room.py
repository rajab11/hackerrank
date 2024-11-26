"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  members per group where  ≠ .

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of  and the room number list.

Input Format

The first line consists of an integer, , the size of each group.
The second line contains the unordered elements of the room number list.


Constraints


Output Format

Output the Captain's room number.

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output

8
Explanation

The list of room numbers contains  elements. Since  is , there must be  groups of families. In the given list, all of the numbers repeat  times except for room number .
Hence, 8 is the Captain's room number.
"""
# Read input
k = int(input())  # Size of each group
rooms = list(map(int, input().split()))  # List of room numbers

# Initialize sets to track rooms
seen_once = set()
seen_multiple = set()

# Process each room number
for room in rooms:
    if room in seen_once:
        # If the room is in seen_once, it should be moved to seen_multiple
        seen_once.remove(room)
        seen_multiple.add(room)
    elif room not in seen_multiple:
        # If the room is not in seen_multiple, add it to seen_once
        seen_once.add(room)

# The only element remaining in seen_once is the Captain's room
print(seen_once.pop())
