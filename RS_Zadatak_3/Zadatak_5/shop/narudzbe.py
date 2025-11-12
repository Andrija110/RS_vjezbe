from .proizvodi import Proizvod, skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi 
        self.ukupna_cijena = ukupna_cijena
    
    def ispis_narudzbe(self):
        """Ispisuje detalje narudžbe."""
        stavke = []
        for proizvod in self.naruceni_proizvodi:
            stavke.append(f"{proizvod.naziv} x {proizvod.dostupna_kolicina})")
        stavke_str = ", ".join(stavke)
        print(f"Narudžba: {stavke_str} | Ukupna cijena: {self.ukupna_cijena:.2f} eura")
    
def napravi_narudzbu(naruceni_proizvodi):
    """
Provjerava valjanost, dostupnost i stvara novu instancu klase Narudzba.
    """
    required_keys = ['naziv', 'cijena', 'narucena_kolicina']

    # PROVJERA VALJANOSTI

    # Mora biti neprazna lista
    if not isinstance(naruceni_proizvodi, list) or not naruceni_proizvodi:
        print("[GREŠKA] Narudžba mora biti neprazna lista proizvoda.")
        return None
    
    for item in naruceni_proizvodi:
        # Svaki element mora biti rječnik
        if not isinstance(item, dict):
            print("[GREŠKA] Svaki element u listi mora biti rječnik.")
            return None
        
         # Svaki rječnik mora sadržavati ključeve
        if not all(key in item for key in required_keys):
            print(f"[GREŠKA] Svaki rječnik mora sadržavati ključeve: {', '.join(required_keys)}.")
            return None
    
    # PROVJERA DOSTUPNOSTI

    for item in naruceni_proizvodi:
        naziv_narucenog = item['naziv']
        kolicina_narucena = item['narucena_kolicina']

        proizvod_u_skladistu = next((p for p in skladiste if p.naziv == naziv_narucenog), None)

        if not proizvod_u_skladistu or proizvod_u_skladistu.dostupna_kolicina < kolicina_narucena:
            print(f"[GREŠKA] Proizvod '{naziv_narucenog}' nije dostupan u traženoj količini ili ne postoji!")
            return None
    
    # IZRAČUN UKUPNE CIJENE

    ukupna_cijena = sum(item['cijena'] * item['narucena_kolicina'] for item in naruceni_proizvodi)

    # STVARANJE NARUDŽBE

    nova_narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append(nova_narudzba)

    print("[INFO] Narudžba uspješno stvorena i pohranjena.")
    return nova_narudzba