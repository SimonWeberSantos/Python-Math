#Rechnungen mit verschiedenen Operatoren mit Def Funktion

#Import
import time
import random
random.seed()

#Funktion
def tryexcept():
    answer = False
    while answer == False:
        try:
            rueckgabe=int(input())
            return rueckgabe
            answer = True
        except:
            print("Bitte geben Sie eine ganze Zahl ein!!!")
            time.sleep(2)
            answer = False

#Variablen
korrekt = 0
versuch = 0

#Loop
while versuch <10:
    a=random.randint(10,20)
    b=random.randint(1,10)
    f=random.randint(1,3)
    c=a-b
    d=a*b
    e=a+b
    print("Rechnen Sie bitte folgendes aus:")
    if f == 1:
        print(a,'-',b)
        
        antwort = tryexcept()
        
        if antwort==int(c):
            print("Bravo, korrektes Ergebnis")
            korrekt = korrekt + 1
            versuch = versuch + 1
        else:
            print("Falsche Anwort - Korrekt wäre:" ,c)
            versuch = versuch + 1
            
    if f == 2:
        print(a,'x',b)
        
        antwort = tryexcept()
        
        if antwort==int(d):
            print("Bravo, korrektes Ergebnis")
            korrekt = korrekt + 1
            versuch = versuch + 1
        else:
            print("Falsche Anwort - Korrekt wäre:" ,d)
            versuch = versuch + 1

    if f == 3:
        print(a,'+',b)
        
        antwort = tryexcept()
        
        if antwort==int(e):
            print("Bravo, korrektes Ergebnis")
            korrekt = korrekt + 1
            versuch = versuch + 1
        else:
            print("Falsche Anwort - Korrekt wäre:" ,e)
            versuch = versuch + 1

print("Sie haben 10 Aufgaben durch.")
print("Korrekt gelöst:", korrekt)
print()
input("Bitte drücken Sie die Eingabetaste (Enter), um das Programm zu schliessen: ")