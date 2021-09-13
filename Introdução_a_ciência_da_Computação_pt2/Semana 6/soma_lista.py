def soma_lista(lista):
    n = len(lista)
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[n-1] + soma_lista(lista[:n-1])
    
    