import sys
from checkArguments import checkArguments

checkArguments(sys, 1)

value1 = sys.argv[1]

# Integer list sorting
# Take a list of integers and print it after sorting it in descending order
#
# Instructions
# Your input variable will contain a list of integers, you have to sort
# the list in descending order and print it.
#   Input
#     value1: The list to sort
#
# Sample Test Cases
# Short list
#   value1: 3,4,-9
#   output: 4,3,-9
#
# Long list:
#   value1: 3,9,10,5,2,7,9,2
#   output: 10,9,9,7,5,3,2,2
#
# Your solution code goes below
