from modules.alimento import Alimento

class Cajon:
    def __init__(self,alimentos=[],p_peso=0):
        self.alimentos = alimentos
        self.peso=self.calcular_peso
        
        
    # def agregaralimento(self, alimento):
    #     if not isinstance(alimento,Alimento ):
    #         raise ValueError("El alimento debe ser una una instancia de la clase Alimento")
    #     self.alimentos.append(alimento)
    
    # def calcular_awprom(self):
    #     if len(self.alimentos) == 0:
    #         raise ValueError("No hay alimentos en el cajón")
    #     suma_aw=0
    #     for i in self.alimentos:
    #         suma_aw+=i.mostrar_aw()
    #     return suma_aw/len(self.alimentos)
    
    # def calcular_peso(self):
    #     if len(self.alimentos) == 0:
    #         raise ValueError("No hay alimentos en el cajón")
    #     suma_peso=0
    #     for i in self.alimentos:
    #         suma_peso+=i.mostar_peso()
    #     return suma_peso/len(self.alimentos)
    
    
    # def calcular_awtipoprom(self,tipo_alimento:str):

    #     if len(self.alimentos) == 0:
    #         raise ValueError("No hay alimentos en el cajón")
    #     suma_aw=0
    #     for i in self.alimentos:
    #         if tipo_alimento == i.mostrar_tipo():
    #             suma_aw+=i.mostrar_aw()
    #     return suma_aw/len(self.alimentos)
    
    # def calcular_aw(self,nombre:str):
    #     if len(self.alimentos) == 0:
    #         raise ValueError("No hay alimentos en el cajón")
    #     suma_aw=0
    #     for i in self.alimentos:
    #         if nombre == i.mostrar_nombre():
    #             suma_aw+=i.mostrar_aw()
    #     return suma_aw/len(self.alimentos)
    