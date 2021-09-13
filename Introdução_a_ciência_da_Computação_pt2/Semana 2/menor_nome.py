def menor_nome(nomes):
    menor = "aaa"*50
    for i in nomes:
        i = i.strip()
        if (len(i) < len(menor)):
            menor = i
    return menor.capitalize()
