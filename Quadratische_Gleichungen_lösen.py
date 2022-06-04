# Quadratische Gleichungen lösen

# Benötigter Import
from sympy.solvers import solve
from sympy import Symbol

# Gleichung sieht so aus
# 3/4(16x+24)+6(3x-4) = 2/3(27x+18)+6x-3
# Lösung ist 2.5

# Für die Berechnung der Lösung muss die Rechnung so umgeformt werden
# dass auf der einen Seite Null steht! Siehe Beispiel unten in der Berechnung:

# Berechnung
x = Symbol('x')
print(solve(3/4*(16*x+24)+6*(3*x-4)-2/3*(27*x+18)-6*x+3, x))

# Neue Berechnung bitte HIER!!! eingeben:
a = (solve(, x)) #Eingabe durch User vor dem Komma
b = round(a[0], 3) #Extrahieren der Zahl aus der Liste + Runden auf drei Stellen
print("Lösung =",b) #Ausgabe