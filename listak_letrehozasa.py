honapok = ['január', 'február', 'március', 'április', 'május', 'június']
# print(type(honapok)) # Típusa
# print(f"A lista hossza: {len(honapok)}") # A lista hossza: len()
# print(honapok[3])
# print(f"Az utolsó elem: {honapok[-1]}")

# az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

# 2-es indexű elemtől a végéig
print(honapok[2:])

print(', '.join(honapok))

# # Lista bejárása: for-range ciklus.
# for i in range(len(honapok)):
#     print(honapok[i])

print('\nHónapok:\n')
for honap in honapok:
    print(honap)

