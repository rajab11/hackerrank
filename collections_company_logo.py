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
    print(char_count)

    #output
    print(' '.join(f"{char} {count}" for char,count in char_count.items()))
