'''class Estudiantes:
    provincia = 'Chaco'

    def __init__(self, nombre, apellido, localidad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.localidad = localidad
        self.dni = dni

lista_estudiantes = list()
estudiante_1 = Estudiantes('Franco', 'Godoy', 'Resistencia, Chaco', '44644703')
otro_estudiante = Estudiantes('Alan', 'Godoy', 'Resistencia, Chaco', '22111002')

lista_estudiantes.append(estudiante_1)
lista_estudiantes.append(otro_estudiante)


for e in lista_estudiantes:
    print(e.nombre)
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Alumno(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando para el grado {self.grado}.")

    def entregar_tarea(self):
        print(f"{self.nombre} ha entregado la tarea.")

    def presentar(self):
        super().presentar()
        print('Y SOY ALUMNO/A')

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def enseñar(self):
        print(f"{self.nombre} está enseñando {self.materia}.")

    def presentar(self):
        super().presentar()
        print('Y SOY PROFESOR/ORA')


e1 = Alumno('Alejandro',30,'quinto')
p1 = Profesor('Nicolas',34,'Programacion')

e1.presentar()
p1.presentar()
