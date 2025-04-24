from modules.alimento import Alimento
import math
class Fruta(Alimento):
    def __init__(self, p_peso, p_tipoalimento, p_aw=0):
        super().__init__(p_peso)
        self.tipo_alimento = p_tipoalimento
        self.aw = p_aw
   
    def mostrar_tipo(self):
        if type(self.tipo_alimento) != str:
            raise ValueError("El tipo de alimento debe ser una cadena de texto")
        return self.tipo_alimento
    
    def definir_ecuacion(self,ecuacion_aw):
        pass
        self.aw=ecuacion_aw
        return self.aw
    
    def mostrar_aw(self):
        if type(self._aw) != float:
            raise ValueError("El valor de aw debe ser un número decimal")
        return self._aw


class Manzana(Fruta):
    def __init__(self, p_peso, p_tipoalimento, p_aw=0,p_nombre="Manzana"):
        super().__init__(p_peso, p_tipoalimento, p_aw)
        self.nombre=p_nombre
        self.valor_aw=0.97*((1-math.exp(-0.1*p_peso)/(1+math.exp(-0.1*p_peso))))

    def mostrarnombre(self):
        if type(self.nombre) != str:
            raise ValueError("El nombre de la papa debe ser una cadena de texto")
        return self.nombre
    
    
    
class Kiwi(Fruta):#math.exp(x)
    def __init__(self, p_peso, p_tipoalimento, p_aw=0,p_nombre="Kiwi"):
        super().__init__(p_peso, p_tipoalimento, p_aw)
        self.nombre=p_nombre
        self.aw=0.96*(1-math.exp(-1800*p_peso)/1+math.exp(-1800*p_peso))
        
    def mostrarnombre(self):
        if type(self.nombre) != str:
            raise ValueError("El nombre de la papa debe ser una cadena de texto")
        return self.nombre