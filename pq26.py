'''How to get list of parameters name from a function in Python?
'''
def fun(a, b, c=10):
    pass

res = fun.__code__.co_varnames[:fun.__code__.co_argcount]
print(res)