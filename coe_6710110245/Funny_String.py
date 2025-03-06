import math
import os
import random
import re
import sys

def funnyString(s):
    r = s[::-1]  # สร้างสตริงย้อนกลับ
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        q = int(input().strip())
        for _ in range(q):
            s = input().strip()
            result = funnyString(s)
            fptr.write(result + '\n')
