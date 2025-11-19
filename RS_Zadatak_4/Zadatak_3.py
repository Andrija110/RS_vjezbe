import asyncio
import time

# Baze podataka
baza_korisnika = [
  {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
  {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
  {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
  {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
  {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
  {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
  {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
  {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

# Korutina 1: Autorizacija
async def autorizacija(korisnik_iz_baze: dict, proslijedjena_lozinka: str) -> str:
    """
    autorizacija provjerom lozinke u bazi. Traje 2 sekunde.
    """
    korisnicko_ime = korisnik_iz_baze['korisnicko_ime']
    print(f"  [Autorizacija]: Pokrenuta provjera lozinke za korisnika {korisnicko_ime}")

    await asyncio.sleep(2)

    ispravna_lozinka = next(
        (item['lozinka'] for item in baza_lozinka if item['korisnicko_ime'] == korisnicko_ime),
        None
    )

    if ispravna_lozinka and proslijedjena_lozinka == ispravna_lozinka:
        return f"Korisnik {korisnicko_ime}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnicko_ime}: Autorizacija neuspješna. (Pogrešna lozinka)"


# Korutina 2: Autentifikacija
async def autentifikacija(korisnik: dict) -> str:
    """
    Autorizacija korisnika provjerom korisničkog imena/emaila.
    """
    ulazno_ime = korisnik['korisnicko_ime']
    ulazni_email = korisnik['email']
    ulazna_lozinka = korisnik['lozinka']

    print(f"\n[Autentifikacija]: Pokrenuta provjera za {ulazno_ime}")

    print(f"[Autentifikacija]: Upit prema bazi podataka (Cloud) za {ulazno_ime}")
    await asyncio.sleep(3)
    print(f"[Autentifikacija]: Podaci dohvaćeni iz Cloud baze.")

    pronadjen_korisnik = next(
        (
            item for item in baza_korisnika
            if item['korisnicko_ime'] == ulazno_ime and item['email'] == ulazni_email
        ),
        None
    )

    if not pronadjen_korisnik:
        return f"Korisnik {ulazno_ime} nije pronađen (Ime/Email neispravni)."
    else:
        print(f"[Autentifikacija]: Korisnik {ulazno_ime} pronađen. Prelazak na autorizaciju...")
        
        rezultat_autorizacije = await autorizacija(pronadjen_korisnik, ulazna_lozinka)
        
        print(f" [Autorizacija]: Provjera za {ulazno_ime} završena.")
        return rezultat_autorizacije

# Glavna funkcija 
async def main():
    print(f"*** Početak simulacije: {time.strftime('%H:%M:%S')} ***")
    
    # 1. Uspješan slučaj 
    uspjesni_korisnik = {
        'korisnicko_ime': 'ana_anic',
        'email': 'aanic@gmail.com',
        'lozinka': 'super_teska_lozinka' 
    }
    
    # 2. Slučaj neuspješne lozinke 
    los_korisnik = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'pogresna_lozinka'  
    }
    
    # 3. Slučaj neuspješne autentifikacije
    nepostojeci_korisnik = {
        'korisnicko_ime': 'petar_peric',
        'email': 'pp@example.com',
        'lozinka': 'bilo_sto'
    }
    
    rezultat1 = await autentifikacija(uspjesni_korisnik)
    print(f"\nREZULTAT 1: {rezultat1}")
    
    rezultat2 = await autentifikacija(los_korisnik)
    print(f"\nREZULTAT 2: {rezultat2}")
    
    rezultat3 = await autentifikacija(nepostojeci_korisnik)
    print(f"\nREZULTAT 3: {rezultat3}")

    print(f"\n*** Kraj simulacije: {time.strftime('%H:%M:%S')} ***")

# Pokretanje event loop-a
if __name__ == "__main__":
    asyncio.run(main())