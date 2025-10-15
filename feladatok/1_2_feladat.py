"""
1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, 
hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! 
Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!

1.3 Feladat
Egészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó 
által megadott szín kerüljön felvételre a listába, 
és csak ezután történjen meg a lista tartalmának kiírása! 
"""

szinek = ["piros", "fehér", "zöld", "sárga"]

felhasznalo = input("Kérek egy színt! ")

if felhasznalo in szinek:
    print("A megadott szín már szerepel a listában!")
else:
    print("A megadott szín még nem szerepel a listában! Beleírtam.")

szinek.append(felhasznalo)

print(f"A lista tartalma: \n{", ".join(szinek)}")