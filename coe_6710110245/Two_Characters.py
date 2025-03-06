import math
import os
import random
import re
import sys

def alternate(s):
    unique_chars = list(set(s))
    max_length = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            
            filtered = [c for c in s if c == char1 or c == char2]
        
            valid = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    valid = False
                    break
            
            if valid:
                max_length = max(max_length, len(filtered))
    
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
