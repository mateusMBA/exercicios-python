def maiusculas(texto=''):
    maiusculas = ''
    for i in texto:
        if (65 <= ord(i) <= 90):
            maiusculas += i
    return maiusculas
