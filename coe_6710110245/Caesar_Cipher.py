import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = []
    k = k % 26 
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                new_char = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
                result.append(new_char)
            else:
                new_char = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
                result.append(new_char)
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()