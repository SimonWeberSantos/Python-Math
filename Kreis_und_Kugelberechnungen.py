#Kreis berechnen

#Importe
import time

#Variablen
pi = float(3.14159265358979)
wiederholung = 'ja'

#Einstiegstext
print('Kreis berechnen')

#Schleife
while wiederholung in ['Ja', 'ja', 'JA', 'jA', 'j', 'J']:
    print('Durchmesser eingeben:')

    try:
        durchmesser = float(input())
    except:
        print('Ungültige Eingabe')
        time.sleep(1)
        continue

    #Berechnungen

    radius = durchmesser / 2
    fläche = radius**2 * pi
    umfang = durchmesser * pi
    volumen = 4 / 3 * pi * radius**3
    oberfläche = durchmesser**2 * pi

    print()
    print('Radius: ', round(radius, 3))
    print('Kreisfläche: ', round(fläche, 3))
    print('Kreisumfang: ', round(umfang, 3))
    print()
    time.sleep(1)
    print('Kugelvolumen: ', round(volumen, 3))
    print('Kugeloberfläche: ', round(oberfläche, 3))
    
    print()
    time.sleep(2)
    print('Wiederholung? (Ja oder Nein eingeben)')
    wiederholung = input()
    print()

input('Zum Beenden des Programms "Enter" drücken')