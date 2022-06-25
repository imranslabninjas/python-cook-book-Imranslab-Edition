def inc(x):
    return x + 1


# now create another function which takes a function as an argument

def operate(function, x):
    result = function(x)
    return result


# here the operate function takes two arguments which are  first one is function and 2nd is a regular function X
# let me cl operate with the inc function
print(operate(inc, 3))
