# Primzahlenfinder

# Eingabe Benutzer
print("Zahl eingeben")
num = int(input())

# Setze den Primzahlenfinder auf False
finder = False

# Ausnahmeregelung für die Zahlen 1 und 2
if num == 2 or num == 3:
    print('Primzahl')
    finder = True

# Schleife für alle möglichen Zahlen (Achtung: Primzahlen dürfen IMMER nur grösser als 1 sein!!!)

for i in range(2, num):
    if num % i == 0:
        print('KEINE Primzahl')
        finder = True
        break

if finder == False:
    print('Primzahl')

input()
