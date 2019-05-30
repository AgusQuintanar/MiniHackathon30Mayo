n = 4
m = 4

matrix = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [1,0,0,0]
]

regiones = []

for x in range(n): #filas
    print("x",x)
    region = []
    for y in range(m): #columnas
        print("y",y)
        if matrix[x][y] == 1:
            print("wuuuuuuuuuuuuuuuuuuuuuuuu")
            region.append(y)
        else:
            if 
            regiones.append(region)
            region = []

print(regiones)