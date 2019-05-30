'''
Function Description

Complete the circularArrayRotation function in the editor below. It should return an array of integers representing the values at the specified indices.

circularArrayRotation has the following parameter(s):

    a: an array of integers to rotate
    k: an integer, the rotation count
    queries: an array of integers, the indices to report

Input Format

The first line contains space-separated integers, , , and , the number of elements in the integer array, the rotation count and the number of queries.

The second line contains space-separated integers, where each integer describes array element (where ).
Each of the subsequent lines contains a single integer denoting , the index of the element to return from .
'''
n = 3 #number of elements in the integer array
k = 2 #rotation count
q = 3 #number of queries. 

a = [1,2,3] #array

queries = [0,1,2]

for x in range(k):
    a.insert(0,a[-1])
    a.pop()

resultado = []
for y in range(len(queries)):
    resultado.append(a[queries[y]])


print(a)
print(resultado)