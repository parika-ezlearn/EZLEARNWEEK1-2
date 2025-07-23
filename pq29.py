'''A function from a function - Python
'''
def fun1(name):
    def fun2():
        return f"Hello, {name}!"
    return fun2

# Get the function returned by fun1()
msg = fun1("shakshi")

# Call the returned function
print(msg())