def one(word='three'):
    return word.capitalize() + ' is the number'


print(one())

two = one
'''
notice i don't use the parentheses : i am not calling function , just putting the function 
'''
print(two())


