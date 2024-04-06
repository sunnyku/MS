#Python 003:
#List_remove_append
Description
Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK' in its place.
Execution Time Limit
15 seconds

import ast,sys
input_list = (sys.stdin.read()).split(',')
# Write code to remove 'SPSS'
input_list.pop()
# Write code to append 'SPARK'
input_list.append('SPARK')
print(input_list)
