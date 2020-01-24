import sys
from checkArguments import checkArguments

checkArguments(sys, 1)

value1 = sys.argv[1]

# Pig Latin Translator
# Take a sentence / phrase in pig latin, translate it to English
#
# Instructions
# Your input variable will contain a sentence/phrase in pig latin.
# Your job is to translate it to english. You add "yay" if the word
# starts with a vowel. Otherwise move the starting consonant
# sequence (w, wr, sch, ...) to the end of the word and add "ay"
# plus a dash.
#
# Input
#     value1: Sentence / phrase in pig latin
#
# Sample Test Cases
# Short phrase
#   value1: ayay imple-say est-tay ase-cay
#   output: a simple test case
#
# Long phrase
#   value1: ig-pay atin-lay isyay usedyay inyay ools-schay o-tay each-tay anguage-lay onstructs-cay
#   output: pig latin is used in schools to teach language constructs
#
# Your solution code goes below
