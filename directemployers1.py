"""
Direct Employers Problem 1
Write a program that prints the numbers from 1 to 100. But for multiples of three write
“Direct” instead of the number, and for the multiples of five write “Employers”. For
numbers which are multiples of both three and five write “DirectEmployers”.
"""


y = ['DirectEmployers', 'Direct', 'Employers']
for x in range(1, 101):
    print(y[0] if (x % 3 == 0 and x % 5 == 0) else y[1] if x%3 == 0 else y[2] if x % 5 == 0 else x)



"""
# That is the same that:

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(y[0])
    if x % 3 == 0:
        print(y[1])
    if x % 5 == 0:
        print(y[2])
    else:
        print(x)
        
"""

