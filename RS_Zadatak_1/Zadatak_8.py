def filtriraj_parne(lista):
    NovaLista = []
    for i in lista:
        if i % 2 == 0:    
            NovaLista.append(i)
    return(NovaLista)

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(Lista))