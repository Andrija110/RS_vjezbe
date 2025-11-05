def ukloni_duplikate(lista):
    NovaLista = []
    for i in lista:
        if i not in NovaLista:
                NovaLista.append(i)
    return(NovaLista)

Lista = [1, 2, 3, 4, 5, 1, 4, 2, 7, 8, 6, 5, 3, 2,]
print(ukloni_duplikate(Lista))