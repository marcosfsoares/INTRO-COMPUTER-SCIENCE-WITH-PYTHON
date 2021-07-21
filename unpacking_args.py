'''def multiply(*args):
    total = 1
    print(args)
    for arg in args:
        total *= arg
    print(total)
    return total

multiply(-1)


def add(x,y):
    return x+y

nums=[3, 5]
print(add(*nums))

nums2 = {'x': 15, 'y': 25}
print(add(**nums2))

def apply(*args, operator):
    print(args)
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply"

print(apply(2,3,4,5,6,operator = '*'))


def muda(*arg):
    print(arg)
    return arg

def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)
'''
####################
def add2(**kwargs):
    soma = 0
    print(kwargs)
    for item in kwargs:
        print(item,kwargs[item])
        soma += kwargs[item]
    return soma

nums=[3, 5]
#print(add2(*nums))

nums2 = {'x': 15, 'y': 25}
print(add2(**nums2))

