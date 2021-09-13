def is_armstrong_number(number):
    numero = str(number)
    exp = len(numero)
    soma = 0
    for i in range(0,exp):
        soma += (int(numero[i]))**exp
    if (soma == number):
        return(True)
    return(False)   
    
