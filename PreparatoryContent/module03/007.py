Tuple
Description
Add the element ‘Python’ to a tuple input_tuple = ('Monty Python', 'British', 1969). Since tuples are immutable, one way to do this is to convert the tuple to a list, add the element, and convert it back to a tuple.

To learn how to convert a list to a tuple, search for it on Google / Stack Overflow etc.
Execution Time Limit
15 seconds

import ast,sys
input_str = sys.stdin.read()
input_tuple = ast.literal_eval(input_str)

# Write your code here
list_2=list(input_tuple)
list_2.append('Python')
tuple_2=tuple(list_2)
# Make sure to name the final tuple 'tuple_2'
print(tuple_2)
