Dict_Error
Description
From a Dictionary input_dict={'Name': 'Monty', 'Profession': 'Singer' }, get the value of a key ‘Label’ which is not a part of the dictionary, in such a way that Python doesn't hit an error. If the key does not exist in the dictionary, Python should return 'NA'.

Execution Time Limit
15 seconds


import ast,sys
input_str = sys.stdin.read()
input_dict = ast.literal_eval(input_str)

answer = input_dict.get('Label','NA')#Type your answer here
print(answer)
