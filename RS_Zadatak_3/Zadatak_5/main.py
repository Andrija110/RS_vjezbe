from shop.proizvodi import dodaj_proizvod, skladiste
from shop.narudzbe import napravi_narudzbu

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

print(" 1. Dodavanje novih proizvoda u skladište ")

# Dodavanje novih proizvoda
for podaci in proizvodi_za_dodavanje:
    dodaj_proizvod(podaci)

print(f"\n[INFO] Ukupno proizvoda u skladištu: {len(skladiste)} (očekivano 6)")
print("-" * 50)

# Ispis svih proizvoda iz liste skladiste
print("\n 2. Ispis cijelog stanja skladišta ")
for proizvod in skladiste:
    proizvod.ispis()
print("-" * 50)

# stanje i provjera narudžbe

naruceni_proizvodi_ok = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
    {"naziv": "Stolac", "cijena": 150, "narucena_kolicina": 5} # Ne postoji u skladištu
]

print ("\n 3. Stvaranje validne narudžbe ")
moja_narudzba = napravi_narudzbu(naruceni_proizvodi_ok)

if moja_narudzba:
    moja_narudzba.ispis_narudzbe()

print("-" * 50)

# Primjer neuspjele narudžbe (zbog prevelike naručene količine)
naruceni_proizvodi_fail = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 11} # Iznad dostupnih 10
]

print("\n 4. Pokušaj neuspjele narudžbe (zbog nedostatka zaliha) ")
napravi_narudzbu(naruceni_proizvodi_fail)