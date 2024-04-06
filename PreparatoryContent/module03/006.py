Nested List
Description
Extract Python from a nested list input_list =  [['SAS','R'],['Tableau','SQL'],['Python','Java']]


Execution Time Limit
15 seconds


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
answer = input_list[2][0] #Type your answer here
print(answer)
