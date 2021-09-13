def is_valid(isbn):
    isbn = isbn.replace('-','')
    numbers = '0123456789'
    
    if(len(isbn) != 10):
        return False
    
    multiplier = 10
    isbn_sum = 0
    
    for i in isbn:

        if (multiplier == 1):
            if (i == 'X'):
                i = 10
            else:
                if i not in numbers:
        
                    return False
        if (str(i) not in numbers and multiplier > 1):
            return False
        
        isbn_sum += int(i)*multiplier
        multiplier -= 1
        
    if isbn_sum % 11 == 0:
        return True
    
    return False
