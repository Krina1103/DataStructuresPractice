"""
Reversing a string using stack
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_list = []
reversed_string = ""
s = stack.Stack()
for i in string:
    s.push(i)

while not s.is_empty():
    reversed_list.append(s.pop())

reversed_string = (''.join(reversed_list))
print(reversed_string)
# Your solution here.


