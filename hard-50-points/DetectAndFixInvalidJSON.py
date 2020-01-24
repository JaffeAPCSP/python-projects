import sys
from checkArguments import checkArguments

checkArguments(sys, 1)

value1 = sys.argv[1]

# Detect and fix invalid JSON
# Take an invalid JSON string and figure out where the errors are and
# make it valid
#
# Instructions
# Your input variable will contain a string of invalid JSON. However,
# each invalid JSON string received can be fixed by making one or
# more single character changes. Only three possible things may
# be wrong with the JSON string: 1) missing leading or trailing
# brace, 2) unquoted JSON string value, 3) missing comma between
# properties.  (Hint: You'll probably need to do some research on
# what JSON is and how it's formatted)
#
# Input
#     value1: A string of invalid JSON
#
# Sample Test Cases
# Single Problem
#   value1: {"name":"em"
#   output: {"name":"em"}
#
# Multiple Problems
#   value1: "name":"em
#   output: {"name":"em"}
#
# Your solution code goes below
