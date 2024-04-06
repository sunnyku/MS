string to list conversion
Description
Convert a string input_str = 'I love Data Science & Python' to a list by splitting it on ‘&’. The sample output for this string will be:
['I love Data Science ', ' Python']
Execution Time Limit
15 seconds


import ast,sys
input_str = sys.stdin.read()

output_list = input_str.split('&') #Type your answer here
print(output_list)
