If-Else
Description
Write a code to check if the string in input_str starts with a vowel or not. Print capital YES  or NO.

For example, if input_str = 'analytics' then, your output should print 'YES'.
Execution Time Limit


import ast,sys
input_str = sys.stdin.read()
vowels=['a','e','i','o','u']
#Write your code here
if input_str[0] in vowels:
    print('YES')
else:
    print('NO')

#Use capital YES or NO
