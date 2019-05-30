
# s: the initial string
# t: the desired string
# k: an integer that represents the number of operations

s = "hackerhappy"
t = "hackerrank"
k = 9


parte_igual = ""
indice_verificacion = 0

for x in range(len(t)):
    if t[x] == s[x]:
        parte_igual += t[x]
        indice_verificacion = x
    else:
         break;

print(parte_igual)

if len(parte_igual) != indice_verificacion + 1:
    print("no")

r = s.replace(parte_igual,'')

k = k -(len(s) - len(parte_igual)) - (len(t) - len(parte_igual))

print(k)

if k >= 0:
    print("yes")
else:
    print("no")
    