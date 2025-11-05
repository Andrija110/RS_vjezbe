def prvi_i_zadnji(lista):
    if len(lista) == 0:
      return None, None
    PrviBroj = lista[0]
    ZadnjiBroj = lista[-1]
    return PrviBroj, ZadnjiBroj

def max_i_min(lista):
    if len(lista) == 0:
        return None, None
    MaxBroj = lista[0]
    MinBroj = lista[0]

    for i in lista:
        if i > MaxBroj:
            MaxBroj = i
    for i in lista:
        if i < MinBroj:
            MinBroj = i
    return MaxBroj, MinBroj


def presjek(skup1,skup2):
    NoviSkup = set()
    for i in skup1:
        if i in skup2:
              NoviSkup.add(i)
    return NoviSkup
      


Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(Lista1))

Lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(max_i_min(Lista2))

Skup1 = {1, 2, 3, 4, 5}
Skup2 = {4, 5, 6, 7, 8}
print(presjek(Skup1,Skup2))