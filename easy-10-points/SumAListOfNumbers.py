import sys
from checkArguments import checkArguments

checkArguments(sys, 1)

value1 = sys.argv[1]

# Sum a list of numbers
# Take a string of comma separated numbers and print out the sum
#
# Instructions
# Your input variable could contain a list of integer values.  Regardless
# of value, you'll need to print out the sum of the list.
#   Input
#     value1: The list of numbers to add
#
# Sample Test Cases
# Short list
#   value1: 2,5,1
#   output: 8
#
# Long list:
#   value1: 3,9,10,5,2,7,9,2
#   output: 47
#
# Your solution code goes below
