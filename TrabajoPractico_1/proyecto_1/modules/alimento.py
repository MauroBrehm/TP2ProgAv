class Alimento:
    def __init__(self, p_peso):
        self.peso = p_peso

    def mostar_peso(self):
        if type(self.peso) != float :
            raise ValueError("El  peso debe ser un número decimal") 
        return self.peso
    
