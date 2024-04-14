List Comprehensions
Description
Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria] using list comprehensions.

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

list_vowel =[x for x in input_list if x[0].lower() in ['a','e','i','o','u'] ]# [Type your answer here]

print(list_vowel)
