"""
For this list [1, 2, 3] return [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
"""

list = [1, 2, 3]
list1 = []
list2 = []
list3 = []

for x in range(1, len(list)+1):
    list1.append(x)
    list2.append(2*x)
    list3.append(3*x)

print([list1, list2,  list3])

"""
Using  List Comprehensions
"""

print([[x, 2*x, 3*x] for x in range(1, len(list)+1)])

