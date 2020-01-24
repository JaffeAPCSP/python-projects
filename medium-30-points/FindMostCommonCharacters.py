import sys
from checkArguments import checkArguments

checkArguments(sys, 1)

value1 = sys.argv[1]

# Find Most CommonCharacters
# Given a string with multiple words, find the most common character
#
# Instructions
# You will be given a string and your job is to find the most
# common character in that string. If there are two characters
# which appear the same amount of times and are the largest
# amount, you should output both separated by a comma in the
# order they first appeared.
#
#   Input
#     value1: A long or short string
#
# Sample Test Cases
# Short phrase
#   value1: A test case
#   output: t,e,s
#
# Long phrase
#   value1: The way this mode works is by looking for the mode of the characters of any given string
#   output: o
#
# Your solution code goes below

