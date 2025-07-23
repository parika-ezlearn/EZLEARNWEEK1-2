'''Sorting Objects of User Defined Class in Python
'''
# User-defined class GFG
class GFG:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return str((self.a, self.b))

# List of objects
a = [GFG("geeks", 1),
     GFG("computer", 3),
     GFG("for", 2),
     GFG("geeks", 4),
     GFG("science", 3)]
     
res = sorted(a , key=lambda x: x.b)
print(res)