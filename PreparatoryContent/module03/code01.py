Description


You are given a list of string elements and asked to return a list which contains each element of the string in title case or in other words first character of the string would be in upper case and remaining all characters in lower case



Sample Input:



['VARMA', 'raj', 'Gupta', 'SaNdeeP']



import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
updated_list = []
for i in input_list:
    updated_list.append(i.title())
print(updated_list)
# Enter your code here. 
