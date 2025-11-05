def obrni_rjecnik(rjecnik):
    
    NoviRjecnik = {}

    for Kljuc, Vrijednost in rjecnik.items():
        NoviRjecnik[Vrijednost] = Kljuc
    return NoviRjecnik

Rjecnik = {"Ime": "Ivan", "Prezime": "Ivic", "Dob": 25}
print(obrni_rjecnik(Rjecnik))