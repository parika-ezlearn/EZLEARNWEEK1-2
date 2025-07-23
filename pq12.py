'''Python - Accessing nth element from tuples in list
'''
l = [(1, 2), (3, 4), (5, 6)]
n = 1  

# Use list comprehension to extract the nth element from each tuple
r = [t[n] for t in l]
print(r)