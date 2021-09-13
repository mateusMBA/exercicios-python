class PhoneNumber:
    def __init__(self, number):
        self.number = self.digits(number)
        self.area_code = self.digits(number)[:3]
        
    def digits(self,number):
        aux = "0123456789"
        digits = ''
        for i in number:
            if i in aux:
                digits += i
    
        if len(digits) < 10 or len(digits) > 11:
            raise ValueError("Invalid Number")
    
        if len(digits) == 11:
            if digits[0] == '1':
                digits = digits[1:]
            else:
                raise ValueError("Invalid Number")
                
        if (int(digits[0]) < 2 or int(digits[3]) < 2):
            raise ValueError("Invalid Number")
        
        return digits
    
    def pretty(self):
        return ('(' + self.number[:3] + ')-' + self.number[3:6] + '-' + self.number[-4:])


