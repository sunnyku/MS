Function
Description
Create a function squared(),  which takes x and y as arguments and returns the x**y value. For e.g., if x = 2  and y = 3 , then the output is 8.
Execution Time Limit

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
x = int(input_list[0])
y = int(input_list[1])

#Write your code here
def squared(x,y):
    return x**y
print(squared(x,y))
