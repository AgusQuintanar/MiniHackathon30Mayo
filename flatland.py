n = 6 #number of cities
m = 6
c = [0,1,2,4,3,5] #indixes of space stations

mayor = 0
c = sorted(c)
for x in range(n):
    mas_cercano = abs(x-c[0])
    for y in range(1,m):
        if mas_cercano == 0:
            break;
        if abs(x-c[y]) < mas_cercano:
            mas_cercano = abs(x-c[y])
    if mas_cercano > mayor:
        mayor = mas_cercano

print(mayor)