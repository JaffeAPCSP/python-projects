import sys
from checkArguments import checkArguments

checkArguments(sys, 1)

value1 = sys.argv[1]

# Roman Numeral Conversion
# Take a roman numeral(<1000 in value) and print its
# corresponding value in the decimal system of numbers.
#
# Instructions
# Your input variable will contain a roman numeral less than
# 1000 in value. Print the corresponding value of the Roman numeral
# in the decimal system of numbers.
#
# Input
#     value1: The Roman numeral
#
# Sample Test Cases
# Small Roman Numeral
#   value1: VI
#   output: 6
#
# Large Roman Numeral
#   value1: CDVII
#   output: 407
#
# Your solution code goes below
