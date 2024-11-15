"""creating an empty list"""
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
"""insering 15 to the list in the second position"""
my_list.insert(1, 15)

"""Extend my_list with another list"""
my_list.extend([50, 60, 70])
"""Remove the last element from my_list"""
my_list.pop()
"""sort my_list in ascending order"""
my_list.sort()
"""find and print index of value 30 in my_list"""
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
print(my_list)
