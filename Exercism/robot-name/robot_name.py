import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Robot:
    
    def __init__(self):
        self.used_names = []
        self.name = self.name_gen()
    
    def name_gen(self):
        while True:
            name = ''
            for i in range(0,5):
                if (i<2):
                    name += random.choice(alphabet)
                else:
                    name += str(random.randrange(1,10))
            if (name not in self.used_names):
                self.used_names.append(name)
                return name        
        
    
    def reset(self):
        self.name = self.name_gen()
        return
