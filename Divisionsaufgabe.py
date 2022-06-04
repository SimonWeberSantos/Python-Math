#Divisionsaufgabe

#Import
import random
random.seed()

#Anzahl Aufgaben
anzahl = False
while anzahl == False:
    try:
        print("Wie viele Divisionsaufgaben möchtest du machen?")
        aufgaben = int(input())
        anzahl = True

    except:
        print("Bitte eine ganze Zahl eingeben!")
        anzahl = False

print()
#Divisionsaufgabe
korrekt = 0
for i in range(1, aufgaben+1):
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = a * b #Nur so kann sichergestellt werden, dass es Lösungen im Integer Bereich gibt

    antwort = False
    
    while antwort == False:
        print("Aufgabe", i, "von", str(aufgaben)+ ":", c, "/", b) # Weil c / b = a oder eben a * b = c
        try:
            eingabe = int(input())
            antwort = True
        except:
            print("Bitte eine ganze Zahl eingeben!")
            continue

    if eingabe == a:
        print("Bravo! Korrektes Ergebnis!")
        korrekt += 1

    else:
        print("Falsch - Korrektes Ergegnis wäre", a, "gewesen.")
        
    print()

print("Von", i, "Aufgaben hast du", korrekt, "korrekt gelöst.")
input()