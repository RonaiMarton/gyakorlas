"""A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, 
a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, 
és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!"""
import random
lista = []

for i in range(1,11):
    lista.append(random.randint(1,3))
print(lista)

valasz = int(input("írjon be egy számot 1-3ig, amit ki szeretne törölni \n"))

while valasz in lista:
    lista.remove(valasz)
print(f"módosított lista: {lista}")