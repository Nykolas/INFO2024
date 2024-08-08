class Coche:
    ruedas = 4
    # Constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f'El coche {self.modelo} esta acelarando')

    @classmethod
    def cambiar_ruedas(cls):
        cls.ruedas = cls.ruedas + 1
        
    @staticmethod
    def calcular_distancia(velocidad,tiempo):
        return velocidad * tiempo

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")
otro_coche = Coche("Ford", "Ranger", "Azul")

mi_coche.acelerar()
Coche.cambiar_ruedas()
print(mi_coche.ruedas)
print(otro_coche.ruedas)
print(Coche.calcular_distancia(80,2))



'''
# Acceder al estado de los atributos directamente
print('Atributos del primer coche:')
print(mi_coche.marca)  # Toyota
print(mi_coche.modelo)  # Corolla
print(mi_coche.color)  # Rojo
print(mi_coche.ruedas)  # 4

print('Atributos del segundo coche:')
print(otro_coche.marca)  # Ford
print(otro_coche.modelo)  # Ranger
print(otro_coche.color)  # Azul
print(otro_coche.ruedas)  # 4
'''