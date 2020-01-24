import sys
from checkArguments import checkArguments

checkArguments(sys, 2)

value1 = sys.argv[1]
value2 = sys.argv[2]

# Zipper merge
# Merge two arrays in a zipper-like fashion
#
# Instructions
# You'll get two inputs, each will be a comma separated list of
# numbers. Each input will contain the same amount of numbers.
# You'll need to merge the two lists by inserting numbers from
# value2 into value1. Each number from value2 should be
# inserted every other number starting after the first number
# in value 1.
#
#   Input
#     value1: First comma separated list of numbers
#     value2: Second comma separated list of numbers
#
# Sample Test Cases
# Short List
#   value1: 9,5
#   value2: 7,10
#   output: 9,7,5,10
#
# Large List
#   value1: 34,18,4,102
#   value2: 15,19,120,64
#   output: 34,15,18,19,4,120,102,64
#
# Your solution code goes below

