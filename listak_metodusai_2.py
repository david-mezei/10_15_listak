honapok = ['január', 'február', 'március', 'április', 'május', 'június']
#honapok = [1,3,5,2]

# sorbarendezi a listát
sorted_honapok = sorted(honapok, reverse=True) # reverse=True --> csökkenő sorrend
print(honapok)
print(sorted_honapok)

# az adott elem első előfordulásának indexe
print(honapok.index('március'))

print("április" in honapok)
