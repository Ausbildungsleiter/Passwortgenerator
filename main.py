#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import random, datetime

# pRNG mit der aktuellen Zeit initialisieren
random.seed(datetime.datetime.now())

# welche Wortliste?
tollewortliste = "tollewortliste.txt"
# Sonderzeichen
#  -> damit die Sonderzeichen überall funktionieren,
#     sollen sie aus dem Zeichensatz US-ASCII stammen,
#     da sie dann auch immer gleich encodiert werden.
fastallesonderzeichen = ':;<=>?@#$%&()*+,-./!"'
# Die besonders besonderen lieber nicht nehmen
sonderzeichen = '+:=!?.,:;-/()#%'

def grossbuchstabenkontrolle ( passwort ):
    grossbuchstaben = 'ABCDEFGHIJKLMNPQRSTUVWX'
    for char in passwort:
        if char in grossbuchstaben:
            # print ("{} ist ein Großbuchstabe.".format(char))
            return passwort
    pw = ''.join((passwort[0].upper(),passwort[1:]))
    return pw

# Einlesen
with open(tollewortliste, "r") as ins:
    liste = []
    for line in ins:
        # print(".",end="")
        liste.append(line.strip())
ins.close()

wortliste = []
for r in range(3):
    zahl = random.randint(0,len(liste)-1)
    wortliste.append(liste[zahl])
    # jetzt ein Sonderzeichen und eine Zahl einfügen
    zahl = random.randint(0,len(sonderzeichen)-1)
    wortliste.append(sonderzeichen[zahl])
    wortliste.append(str(random.randrange(0,100)))

result = ''.join(wortliste)
result = grossbuchstabenkontrolle(result)
print ("\nDeine neuen Wörter, die zusammen ein gutes Passwort ergeben:\n\n\t",end="")
print (result)
print ("\nSicherheitshalber wurden die Zwischenräume mit Sonderzeichen gefüllt.\n")
print ("Dein generiertes Geheimnis ist {} Zeichen lang.".format(len(result)))
print ("")
