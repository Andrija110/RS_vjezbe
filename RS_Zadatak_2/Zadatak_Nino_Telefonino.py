#%%
from pathlib import Path

def ucitaj_iz_datoteke(datoteka: Path, vrsta:str) -> dict:
    lista = datoteka.read_text(encoding="utf-8").splitlines()
    rezultat = dict()
    for linija in lista:
        linija_splitano = linija.split()
        pozivni = linija_splitano[0]
        ostalo = ' '.join(linija_splitano[1:])
        rezultat[pozivni] = ostalo, vrsta
    return rezultat

def ucitaj_brojeve():
    baza = dict()

    file_fiksni=Path("lista_brojeva_fiksni.txt")
    fiksni_brojevi=ucitaj_iz_datoteke(file_fiksni, "fiksna mreža")
    file_mobilni=Path("lista_brojeva_mobilni.txt")
    mobilni_brojevi=ucitaj_iz_datoteke(file_mobilni, "mobilna mreža")
    file_posebni=Path("lista_brojeva_posebni.txt")
    posebni_brojevi=ucitaj_iz_datoteke(file_posebni, "posebna mreža")

    for broj in fiksni_brojevi:
        baza[broj] = fiksni_brojevi[broj]
    for broj in mobilni_brojevi:
        baza[broj] = mobilni_brojevi[broj]
    for broj in posebni_brojevi:
        baza[broj] = posebni_brojevi[broj]

    return baza

    
def ciscenje(broj: str)->str:
    """
    Čistimo telefonski broj od svih nepotrebnih znakova
    """
    # Proći kroz sve znakove, ako ima bilo što što nije broj ili razmak ili () ili - / onda nije valjan
    rezultat=''

    for znak in broj:
        j = len(rezultat)
        
        if znak=='+' and j==0:
            continue
        elif znak in ['(', ')', '-', '/']:
            continue 
        elif znak.isspace():
            continue
        elif znak.isdigit():
            rezultat+=znak
        else:
            return None
        
    return rezultat

def validacija(broj: str, baza: dict):
    """
    provjeravamo telefonski broj 
    """
    prva_nula = True
    if broj.startswith('385'):
        broj = broj[3:]  # maknemo pozivni za HR
        prva_nula = False
    elif broj.startswith('00385'):
        broj = broj[5:]  # maknemo pozivni za HR
        prva_nula = False

    if not prva_nula:
        broj = '0' + broj  # dodamo nulu na početak

    # Kada dobiješ kandidata za pozivni broj 
    # provjeri da li postoji u bazi
    pozivni_broj = broj[:2]  # primjer uzimamo prva dva broja
    ostatak_broja = broj[2:]

    if baza.get(pozivni_broj) is not None:        # if pozivni_broj in baza
        return pozivni_broj, ostatak_broja               

    pozivni_broj = broj[:3]
    ostatak_broja = broj[3:]
    if baza.get(pozivni_broj) is not None:
        return pozivni_broj, ostatak_broja  # if pozivni_broj in baza
    
    return None, None  


def validiraj_broj_telefona(broj: str)->dict:
    """
    Glavna funkcija koja provjerava broj
    """
    baza = ucitaj_brojeve()

    cisti_broj = ciscenje(broj)
    if cisti_broj is None:
        return {
            "validan": False,            
        }
    
    pozivni, ostatak = validacija(cisti_broj, baza)
    if pozivni is not None:        
        rezultat = {
            "pozivni_broj": pozivni,
            "broj_ostatak": ostatak,           
        }
        mjesto_operater, vrsta = baza[pozivni]
        if vrsta == "fiksna mreža":
            rezultat["mjesto"] = mjesto_operater
            rezultat["operater"] = None
            if len(ostatak) < 6 or len(ostatak) > 7:
                rezultat["validan"] = False
            else:
                rezultat["validan"] = True
        elif vrsta == "mobilna mreža":
            rezultat["operater"] = mjesto_operater
            rezultat["mjesto"] = None
            if len(ostatak) < 6 or len(ostatak) > 7:
                rezultat["validan"] = False
            else:
                rezultat["validan"] = True
        else:
            rezultat["operater"] = mjesto_operater
            rezultat["mjesto"] = None
            if len(ostatak) != 6:
                rezultat["validan"] = False
            else:
                rezultat["validan"] = True
        return rezultat
    else:
        rezultat = {
            "validan": False,  
        }

    return rezultat
#%%
def testiranje():
    while True:
        broj = input("Upiši broj: ")
        rezultat = validiraj_broj_telefona(broj)
        print(rezultat)

if __name__ == "__main__":
    testiranje()