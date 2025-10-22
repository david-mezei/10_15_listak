"""
1. feladat, 3. feladat
Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!
Az adott lista elemei közül a program kiírja a 3-mal osztható páros számokat! 
"""

harommal_oszthato = []
hattal_oszthato = []
for i in range(1,41):
    if i % 3 == 0:
        harommal_oszthato.append(i)
    if i % 6 == 0:
        hattal_oszthato.append(i)

    
print(f"Az [1;40] intervallumon a 3-mal osztható számok listája:\n{harommal_oszthato}")
print(f"Az [1;40] intervallumon a 3-mal osztható páros számok listája:\n{hattal_oszthato}")