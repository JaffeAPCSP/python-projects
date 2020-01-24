import sys
from checkArguments import checkArguments

checkArguments(sys, 1)

value1 = sys.argv[1]

# Find Longest Word
# Given a string with multiple words, return the longest word.
#
# Instructions
# You'll get one input, a string with multiple words. Return
# the longest word in the string. If the input contains multiple
# words that are the largest length, return a string that contains
# all of the words in the same order they are provided. All
# returned strings should be lowercase and trimmed of whitespace.
#
#   Input
#     value1: Single string with multiple words
#
# Sample Test Cases
# Regular
#   value1: run,barn,yellow,barracuda,shark,fish,swim
#   output: barracuda
#
# Same Size
#   value1: fishes,sam,gollum,sauron,frodo,balrog
#   output: fishes,gollum,sauron,balrog
#
# Your solution code goes below
