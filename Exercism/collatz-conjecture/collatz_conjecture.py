def steps(number):
    if number <= 0:
        raise ValueError("Number is not valid!")
    
    stp = 0
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3*number + 1
        stp += 1
    
    return stp

