def multiplos(number):
    return [i for i in range(1,number//2 + 1) if number%i == 0]
        

def classify(number):
    if number < 1:
        raise ValueError("Invalid Number")
    multiplos_list = multiplos(number)
    if sum(multiplos_list) == number:
        return 'perfect'
    else:
        if sum(multiplos_list) > number:
            return 'abundant'
        else:
            return 'deficient'
        

