"""
The first stop light turn red every 5 minute
 the second turn red every 3 minutes
 the third turn red every 9 minutes
 the fourth turn red every 8 minutes
how many time at day all the lights turn red. And in what minutes.

"""

"""
MY LCM MAT WAY:
5-9-3-8
-----------
5-9-3-4 = 2
5-9-3-2 = 2
5-9-3-1 = 2
5-3-1-1 = 3
5-1-1-1 = 3
1-1-1-1 = 5
-----------
LCM is 2 *2 *2 *3 *3 *5 = 360 
"""

"""
MAT way to calculate minutes in a day:
1 day = 24 hours
1 horas = 60 minutes
then 24*60 = 1440 minutes in a day
"""

# PYTHON WAY TO FOUND LCM

from math import gcd

a = [3, 5, 8, 9]   #will work for an int array of any length


def LCMULT(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

"""
Solved the problem with or function LCMUT
"""
l= []
count = 0
for x in range(1, 1441):
    if x % LCMULT(a) == 0:
        count = + count+1
        l.append(x)
print(l, count)


"""
If you don't know LCM don't worry use this:
"""
l = []
count = 0
for x in range(1, 1441):
    if x % 3 == 0 and x % 5 == 0 and x % 8 == 0 and x % 9 == 0:
        count = + count + 1
        l.append(x)

print(l, count)


"""
Using functions:
"""


def count_times(a):
    l = []
    count = 0
    for x in range(1, 1441):
        if x % LCMULT(a) == 0:
            count = + count+1
            l.append(x)
    return l, count


print(count_times([3, 5, 8, 9]))


