import sys
from checkArguments import checkArguments

checkArguments(sys, 2)

value1 = sys.argv[1]
value2 = sys.argv[2]

# Fibonacci Numbers
# Start with one Fibonacci sequence number, then calculate more from there.
#
# Instructions
# Your input variable will contain a fibonacci sequence number. Your
# job is to calculate the next n digits.  (Hint: Look up the definition
# of Fibonacci numbers)
#
#   Input
#     value1: The starting number
#     value2: n numbers to calculate after value1
#
# Sample Test Cases
# Small Numbers
#   value1: 5
#   value2: 2
#   output: 8,13
#
# Large Numbers
#   value1: 34
#   value2: 7
#   output: 55,89,144,233,377,610,987
#
# Your solution code goes below

