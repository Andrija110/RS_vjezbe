class Proizvod:
    """Klasa koja predstavlja proizvod u skladištu."""
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        """Ispisuje sve atribute proizvoda."""
        print(f"  > {self.naziv} | Cijena: {self.cijena:.2f} | Količina: {self.dostupna_kolicina}")

    def __repr__(self):
        """Poboljšana reprezentacija objekta."""
        return f"Proizvod('{self.naziv}', {self.cijena}, {self.dostupna_kolicina})"
    
def dodaj_proizvod(dodaci_proizvoda):
    """
    dodajte proizvod u skladište.
    """
    novi_proizvod = Proizvod(
        naziv=dodaci_proizvoda["naziv"],
        cijena=dodaci_proizvoda["cijena"],
        dostupna_kolicina=dodaci_proizvoda["dostupna_kolicina"]
    )
    skladiste.append(novi_proizvod)