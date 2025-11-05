import random

broj = random.randint(1, 100)
pokusaji = 0

print("Pogodi broj između 1 i 100.")

while pokusaji != broj:
    unos = int(input("Unesite vaš pokušaj: "))
    pokusaji += 1

    if unos < broj:
        print("Broj je manji!")
    elif unos > broj:
        print("Broj je veći!")
    else:
        print(f"Čestitamo! Pogodili ste broj {broj} u {pokusaji} pokušaja.")
        break