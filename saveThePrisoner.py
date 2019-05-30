n = 5 #number of prisoners
m = 2 #number of sweets
s = 2 #the chair number to begin passing out sweets from 

'''
The first line contains an integer, , denoting the number of test cases.
The next lines each contain space-separated integers:
- : the number of prisoners
- : the number of sweets
- : the chair number to start passing out treats at 
'''

if (s + m%n - 1)%n == 0:
    print(n)
else:
    print((s + m%n - 1)%n)


