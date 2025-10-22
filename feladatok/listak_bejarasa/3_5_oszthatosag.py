csak_harom = []
csak_ot = []
mindketto = []

for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        mindketto.append(i)
    elif i % 3 == 0:
        csak_harom.append(i)
    elif i % 5 == 0:
        csak_ot.append(i)

print(f"Csak hárommal osztható:\n{csak_harom}")
print(f"Csak öttel osztható:\n{csak_ot}")
print(f"Mindkettővel osztható:\n{mindketto}")