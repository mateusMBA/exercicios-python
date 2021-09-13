def incomodam(n):
    if n <= 0:
        return ''
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n <= 0:
        return ''
    if n == 1:
        return 'Um elefante incomoda muita gente\n'
    if n == 2:
        return elefantes(n-1) + F'{n} elefantes ' + incomodam(n) + 'muito mais\n'
    return (elefantes(n-1) + F'{n-1} elefantes incomodam muita gente\n{n} elefantes ' + incomodam(n) + 'muito mais\n')

        
