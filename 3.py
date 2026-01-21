"""Írj egy programot, amely a felhasználótól betűket kér be mindaddig, amíg az nem ad meg betűt, csupán egy ENTER-t üt!

A program vizsgálja meg a megadott betűt, és tárolja el egy listában, ha az még nem szerepel benne 
(a felhasználó korábban még nem adta meg)! A program NE különböztesse meg a kis- és nagybetűket egymástól, 
de olyan formában tárolja el a betűket mindig, ahogy a felhasználó megadta.

Ha a megadott betű már szerepel a listában írja ki, a képernyőre, hogy "Ezt a betűt már rögzítettem."!

Minden egyes adatbekérés után írja ki a már rögzített betűket ábécé sorrendben (elöl a nagybetűk, utána a kisbetűk ábécé sorrendben)!
"""

lista = []

futas = True

while futas:
    valasz = input("adjon meg egy betűt, majd nyomjon egy entert ha ki akar lépni \n")
    if valasz == "":
        futas = False
    else:
        lista.append(valasz)
        lista.sort()
        if lista.count(valasz) > 1:
            lista.remove(valasz)
            print("ezt a valászt már rögzítettem")
        print(lista)