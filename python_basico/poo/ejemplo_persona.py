class Estudiantes:
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