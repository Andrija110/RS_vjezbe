godina_unos = input("Unesite godinu: ")
godina = int(godina_unos)

prijestupna = (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0)

if prijestupna:
    print(f"Godina {godina} je prijestupna.")
else:
    print(f"Godina {godina} nije prijestupna.")