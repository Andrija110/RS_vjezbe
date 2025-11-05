zbroj = 0
print("Unesite cijele brojeve, Za kraj unesite 0.")
while True:
    unos = int(input("Unesite broj: "))
    if unos == 0:
        break
    zbroj += unos
print("Zbroj unesenih brojeva je:", zbroj)