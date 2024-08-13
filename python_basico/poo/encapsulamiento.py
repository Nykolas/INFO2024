class Persona:
    def __init__(self, nombre, edad,dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_edad(self):
        return self.__edad
    
    def set_edad(self,nueva_edad):
        if nueva_edad > 18:
            self.__edad = nueva_edad
    
    def presentar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.__edad} años.")

p1 = Persona('Nicolas',34,36363636)

print(p1.get_edad()) #Rompe la idea de encapsulamiento
p1.set_edad(30)
print(p1.get_edad())

p1.presentar()

