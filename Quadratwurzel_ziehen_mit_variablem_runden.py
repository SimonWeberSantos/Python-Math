# Zahl eingeben, aus der die Quadratwurzel gezogen werden soll
a = 23

# Anzahl Nachkommastellen eingeben
nachkomma = 5

x0 = 0.001
y0 = a / x0
x1 = (x0+y0) / 2
y1 = a / x1
erst = (x1+y1) / 2
zweit = a / erst

for i in range(1000):
    dritt = (erst + zweit) / 2
    viert = a / dritt
    erst = dritt
    zweit = viert
quadratwurzel = viert

print('Quadratwurzel von', a, '=', round(quadratwurzel, nachkomma))