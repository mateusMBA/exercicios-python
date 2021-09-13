def square_of_sum(number):
    square_sum = 0
    for i in range(1,number+1):
        square_sum += i
    return square_sum**2


def sum_of_squares(number):
    sum_squares = 0
    for i in range(1,number+1):
        sum_squares += i**2
    return sum_squares


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
    
