'''
maximizingXor has the following parameter(s):

    l: an integer, the lower bound, inclusive
    r: an integer, the upper bound, inclusive
'''

l = 11
r = 100

mayor = 0

for x in range(l,r+1):
    for y in range(x,r+1):
        if x ^ y > mayor:
            mayor = x ^ y

print(mayor)