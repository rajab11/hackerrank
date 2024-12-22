import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
     words=s.split()
     capitalized_words=[word[0].upper()+word[1:].lower() for word in words]
     capitalized_text=" ".join(capitalized_words)
     return capitalized_text

if __name__ == '__main__':
    #os.environ['OUTPUT_PATH'] = 'output.txt'  # Or another file name
    fptr =open('output.txt', 'w')

    s = input()
    result = solve(s)

    fptr.write(result + '\n')
    fptr.close()