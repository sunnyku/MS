Creating a List Comprehension
Description
You are given an integer 'n' as the input. Create a list comprehension containing the squares of the integers from 1 till n^2 (including 1 and n), and print the list. 

For example, if the input is 4, the output should be a list as follows:

[1, 4, 9, 16]

The input integer 'n' is stored in the variable 'n'.  


Execution Time Limit


import ast, sys
n = int(input())
squares_list = [x**2 for x in range(1,n+1)]
print(squares_list)
# Write your code here (remember to print the list)

