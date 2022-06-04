# Berechnung_Rechteck

# Importe
import time

# Einstieg
print('Fläche eines Rechtecks ausrechnen')
time.sleep(1.5)

# Initialisierung Schleife
a = 1  # Länge
b = 1  # Breite
answer = 'Ja'

# Schleife mit Eingabe
while a and b > 0:
    while answer == 'Ja' or answer == 'ja':
        print('Bitte geben Sie zuerst die Länge in cm ein:')
        try:
            a = float(input())
        except:
            print('Bitte geben Sie eine gültige Zahl >0 ein:')
            time.sleep(1.5)
            continue

        print('Bitte geben Sie die Breite in cm ein:')
        try:
            b = float(input())
        except:
            print('Bitte geben Sie eine gültige Zahl >0 ein:')
            time.sleep(1.5)
            continue

    # Ausgabe + Runden auf drei Stellen
        print('Die Fläche Ihres Rechtecks beträgt', round(a*b, 3), 'cm2')
        time.sleep(2)
        print()
        print('Möchten Sie noch eine Fläche ausrechnen?')
        answer = input()
    a = 0

input('Danke und bis zum nächsten Mal')
