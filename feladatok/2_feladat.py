"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, 
a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot 
[1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából, 
majd írja ki a módosított listát a képernyőre! 
"""

import random as r

szamok = []

for i in range(1, 11):
    velszam = r.randint(1, 3)
    szamok.append(velszam)

print(f"Az eredeti lista:\n{szamok}")

felhasznalo = int(input("Adj meg egy számot [1;3] intervallumon! "))

if felhasznalo in szamok:
    while felhasznalo in szamok:
        szamok.remove(felhasznalo)

    print(f"Rendben, kitöröltem a megadott számot! A módosított lista:\n{szamok}")
else: 
    print("Kérlek a megfelelő intervallumon adj meg számot!")