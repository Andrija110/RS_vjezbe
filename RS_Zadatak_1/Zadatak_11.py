def grupiraj_po_paritetu (lista):

    ParnaLista = []
    NeparnaLista = []

    for i in lista:
        if i % 2 == 0:
            ParnaLista.append(i)
        else:
            NeparnaLista.append(i)
    
    Rjecnik = {'Parni': ParnaLista, 'Neparni': NeparnaLista}
    return Rjecnik

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(Lista))