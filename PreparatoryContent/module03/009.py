Getting a Value from a Dictionary.
Description
Extract the company headed by Tim Cook from the dictionary {'Jack Dorsey': 'Twitter', 'Tim Cook': 'Apple','Jeff Bezos': 'Amazon','Mukesh Ambani': 'RJIO'}
Execution Time Limit
15 seconds

import ast,sys
input_str = sys.stdin.read()
input_dict = ast.literal_eval(input_str)

name = input_dict.get('Tim Cook')#Type your answer here
print(name)
