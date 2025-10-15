honapok = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus', 'szeptember', 'október', 'november']

# Elem hozzáadása lista végére
honapok.append('december')
print(f"A műveletek előtt a listánk: \n{', '.join(honapok)}")

# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
honapok.pop()
print(f"Utolsó hónap törlése után a lista:\n{', '.join(honapok)}")
torolt_honap = honapok.pop()
print(f"Utolsó hónap: {torolt_honap}")


# Adott indexű elem kitörlése:
honapok.pop(0) 
print(f"0-dik index törlése után:\n{', '.join(honapok)}")

# Törlés érték alapján
honapok.remove("február")
print(f"Február törlése után: \n{', '.join(honapok)}")

#Beszúrás adott helyre: 
honapok.insert(0, 'február')
print(f"Február visszarakása után: \n{', '.join(honapok)}")

# del honapok[2]
# print(f"Második index törlése után: \n{', '.join(honapok)}")

# Lista kiürítése
honapok.clear()
print(f"Kiürítés után: \n{honapok}")