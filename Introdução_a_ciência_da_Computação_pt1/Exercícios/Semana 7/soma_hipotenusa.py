def éhipotenusa(x):
    i = 1
    while i < x:
        j = 1
        while j < x:
            if((i**2)+(j**2) == x**2):
                return True
                
            j += 1
        i += 1
    return False

def soma_hipotenusas(n):
    num = 1
    soma = 0
    while num <= n:
        if éhipotenusa(num):
            soma += num
        num += 1
    return soma
    