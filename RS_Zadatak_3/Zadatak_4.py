#%%
# 1. Definirajte klasu Automobil s atributima marka, model, godina_proizvodnje i kilometraža. Dodajte metodu ispis koja će ispisivati sve atribute automobila.
from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def starost_automobila(self):
        trenutna_godina = datetime.now().year
        return trenutna_godina - self.godina_proizvodnje

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")
    
moj_auto = Automobil(
    marka="Audi",
    model="A4",
    godina_proizvodnje=2018,
    kilometraza=10000
)

moj_auto.ispis()

print(f"Starost automobila: {moj_auto.starost_automobila()} godina")
#%%
# 2. Definirajte klasu Kalkulator s atributima a i b. Dodajte metode zbroj, oduzimanje, mnozenje, dijeljenje, potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno."

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        if self.a >= 0:
            return self.a ** 0.5
        else:
            return "Nije moguće izračunati korijen negativnog broja."

kalkulator = Kalkulator(16, 4)

print("Zbroj:", kalkulator.zbroj())
print("Oduzimanje:", kalkulator.oduzimanje())
print("Množenje:", kalkulator.mnozenje())
print("Dijeljenje:", kalkulator.dijeljenje())
print("Potenciranje:", kalkulator.potenciranje())
print("Korijen:", kalkulator.korijen())
#%%
# 3. Definirajte klasu Student s atributima ime, prezime, godine i ocjene.

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        if len(self.ocjene) == 0:
            return 0
        return sum(self.ocjene) / len(self.ocjene)

    def __repr__(self):
        return f"Student({self.ime} {self.prezime}, Prosjek: {self.prosjek():.2f})"

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenski_objekti = [Student(**student) for student in studenti]

for student in studenski_objekti:
    print(student)

najbolji_student = max(studenski_objekti, key=lambda s: s.prosjek())
print(f"Student s najboljim prosjekom: {najbolji_student.ime} {najbolji_student.prezime}")
print(f"Prosjek najboljeg studenta: {najbolji_student.prosjek():.2f}")
# %%
# 4. Definirajte klasu Krug s atributom r. Dodajte metode opseg i povrsina koje će računati opseg i površinu kruga.

import math

class Krug:
    def __init__(self, r):
        if r < 0:
            raise ValueError("Polumjer ne može biti negativan.")
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * (self.r ** 2)

krug = Krug(5)
print(f"Opseg kruga: {krug.opseg():.2f}")
print(f"Površina kruga: {krug.povrsina():.2f}")
#%%
# 5. Definirajte klasu Radnik s atributima ime, pozicija, placa. Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija}".

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"{self.ime} radim na poziciji: {self.pozicija}.")

    def __repr__(self):
        return f"Radnik({self.ime}, Placa: {self.placa:.2f})"

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"{self.ime} radi na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        self.placa += povecanje
        print(f"Trenutna plaća radnika {radnik.ime}: {radnik.placa:.2f}")
        radnik.placa += povecanje
        print(f"Nova plaća radnika {radnik.ime}: {radnik.placa:.2f}")
    
    def __repr__(self):
        return f"Manager({self.ime}, Department: {self.department}, Placa: {self.placa:.2f})"