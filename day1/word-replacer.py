#!/usr/bin/env python3

import re
import sys

numbers_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def findDigits(text):
    firstDigit = findDigit(text, False)
    lastDigit = findDigit(text[::-1], True)
    
    return firstDigit + lastDigit

def findDigit(text, reversed):
    digitFound = False
    countForward = 0
    digit = None
    while (not digitFound and countForward < len(text)):
        if (text[countForward].isdigit()):
            digitFound = True 
            digit = text[countForward]
        else:
            substring = text[countForward:]
            for number in numbers_mapping.keys():
                pattern = number
                if (reversed):
                    pattern = number[::-1]
                hasMatch = re.search(r'^' + pattern + "*", substring)
                if (hasMatch):
                    digitFound = True 
                    digit = str(numbers_mapping[number])
        countForward = countForward + 1
    return digit

for line in sys.stdin:
    newString = findDigits(line)
    if (len(newString) > 0):
        print (newString)
