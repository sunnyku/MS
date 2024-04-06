List to String
Description
Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] to a string using ‘&’. The sample output of this string will be:
Pythons syntax is easy to learn & Pythons syntax is very clear

Note that there is a space on both sides of '&' (as usual in English sentences).
Execution Time Limit
15 seconds

import ast,sys
input_str = (sys.stdin.read()).split(',')

string_1 = input_str[0] + ' & ' + input_str[1]#Type your answer here
print(string_1)
