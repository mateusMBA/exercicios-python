def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Wrong interval!")
    
    aux = 0
    factor = []
    for i in range(min_factor,max_factor + 1):
        for j in range(min_factor,max_factor + 1):
            num = i*j
            if str(num) == str(num)[::-1]:
                if num > aux:
                    aux = num
                    factor = [[i,j]]
                elif num == aux and [j,i] not in factor:
                    factor.append([i,j])
    
    if aux == 0:
        aux = None

    return aux,factor

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Wrong interval!")

    aux = 10**4
    factor = []
    for i in range(min_factor,max_factor + 1):
        for j in range(min_factor,max_factor + 1):
            num = i*j
            if str(num) == str(num)[::-1]:
                if num < aux:
                    aux = num
                    factor = [[i,j]]
                elif num == aux and [j,i] not in factor:
                    factor.append([i,j])

    if aux == 10**4:
        aux = None
    
    return aux,factor
