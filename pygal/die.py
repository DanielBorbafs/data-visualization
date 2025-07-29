from random import randint

class Die():
    """Uma classe que representa um único dado"""
    def __init__(self, num_sides=6):
        """Supõe que seja um dado de seies lados"""
        self.num_sides = num_sides 

    def roll(self):
        """devolve o valolr aleatório entre 1 e o número de lados"""
        return randint(1, self.num_sides) 