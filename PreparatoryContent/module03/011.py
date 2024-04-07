Set_diff
Description
Find the difference, using difference and symmetric_difference, between two given lists - list1 and list2.

First, convert the lists into sets and store them as set_1 and set_2. Then store the difference and symmetric difference in answer_1 and answer_2 respectively. Print both the answers as sorted lists, i.e. convert the final sets to lists, sort it and then return it.
Execution Time Limit
15 seconds

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0]
list_2 = input_list[1]

set_1 = set(list_1) #Type your answer here
set_2 = set(list_2) #Type your answer here
answer_1 = sorted(list(set_1.difference(set_2))) #Type your answer here
answer_2 = sorted(list(set_1.symmetric_difference(set_2))) #Type your answer here
print(answer_1)
print(answer_2)
