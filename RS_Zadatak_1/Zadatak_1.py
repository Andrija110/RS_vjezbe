broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /): ")
rezultat = None

if operator == "+":
    rezultat = broj1 + broj2
elif operator == "-":
    rezultat = broj1 - broj2
elif operator == "*":
    rezultat = broj1 * broj2
elif operator == "/":
    if broj2 != 0:
        rezultat = broj1 / broj2
    else:
        rezultat = "Dijeljenje s nulom nije dozvoljeno."
else:
    rezultat = "Nepoznat operator."

print("Rezultat:", rezultat)
