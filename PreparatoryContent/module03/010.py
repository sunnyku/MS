List of Values in a Dictionary.
Description
Create a SORTED list of all values from the dictionary input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}
Execution Time Limit
15 seconds
import ast,sys
input_str = sys.stdin.read()
input_dict = ast.literal_eval(input_str)

value_list = list(input_dict.values()) #Type you answer here
print(sorted(value_list))
