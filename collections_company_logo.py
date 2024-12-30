import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    #input
    s = input()

    char_count=Counter(s)
    
    sorted_characters=sorted(char_count.items(),key=lambda x:(-x[1],x[0]))

    #output
    for char,count in sorted_characters[:3]:
        print(char,count)
