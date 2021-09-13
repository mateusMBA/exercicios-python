def encontra_impares(lista,lista_impar=[]):
    n =  len(lista)
    
    if n == 1:
        if (lista[n-1] % 2 != 0):
            lista_impar.append(lista[n-1])
        return lista_impar
   
    if (lista[n-1] % 2 != 0):
        lista_impar.append(lista[n-1])
        return encontra_impares(lista[:n-1])
    else:
        return encontra_impares(lista[:n-1])
    