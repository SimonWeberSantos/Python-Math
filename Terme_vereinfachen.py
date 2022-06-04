# Terme vereinfachen

# Import
import sympy as sy

# Variablen welche im Term vorkommen, müssen hier definiert werden
a = sy.S('a')
b = sy.S('b')
c = sy.S('c')
x = sy.S('x')
y = sy.S('y')
z = sy.S('z')

# Rechnung (in Klammer schreiben)
a = sy.simplify(4*a**2-(3*a**2-b-(2*a**2+a*b-3*b**2)))

# Lösung
print("Lösung =", a)