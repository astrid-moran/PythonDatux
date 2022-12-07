dias = float(input('Días demorados: '))
mora=0.0

if dias>=1 and dias<= 10:
    mora=mora+0.05
elif dias>=1 and dias<=30:
    mora=mora+0.08
elif dias>30:
    mora=mora+0.1


print(mora)