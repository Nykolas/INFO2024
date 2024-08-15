from datetime import datetime

class Libro():
    def __init__(self, titulo, autor, isbn, paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.genero = genero
        self.__prestado = False
        self.__historial_prestamos = [] # Creamos una lista para guardar los préstamos de libros

    def prestar(self, lector): 
        if self.__prestado: # Atributo privado
            print('El libro ya está prestado.')
            return
        if not lector.tiene_permiso:
            print('El lector no tiene permiso para prestar este libro.')
            return
        self.__prestado = True
        self.__historial_prestamos.append((lector.nombre, datetime.now())) # Se guardan los datos del préstamo en la lista
        print(f'El libro {self.titulo} ha sido prestado a {lector.nombre}.')

    def historial_prestamos(self): 
        return [(lector, fecha_prestamo.strftime('En la fecha %d/%m/%Y, a las %H:%M:%S'))
            for lector, fecha_prestamo in self.__historial_prestamos]

    def devolver(self): 
        self.__prestado = False 
        print(f"El libro {self.titulo} ha sido devuelto.")


class Lector():
    def __init__(self, nombre, edad, direccion, numero_socio, tiene_permiso=True):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numero_socio = numero_socio
        self.tiene_permiso = tiene_permiso  

    def solicitar_prestamo(self, libro):
        libro.prestar(self)


class Libreria():
    def __init__(self):
        self.libros = []
        self.lectores = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_lector(self, lector):
        self.lectores.append(lector)

    def mostrar_libros(self):
        print('Libros en la biblioteca:')
        for libro in self.libros:
            print(f"- {libro.titulo} por {libro.autor}")

    def mostrar_lectores(self):
        print("Lectores registrados:")
        for lector in self.lectores:
            print(f"- {lector.nombre}")


class LibroElectronico(Libro): #Herencia
    def __init__(self, titulo, autor, isbn, paginas, genero, formato):
        super().__init__(titulo, autor, isbn, paginas, genero)
        self.formato = formato

    def prestar(self): # Polimorfismo
        # Lógica específica para prestar un libro electrónico
        print(f'El libro electrónico {self.titulo} ha sido enviado por correo electrónico.')

class LibroAudiovisual(Libro):
    def __init__(self, titulo, autor, isbn, duracion, formato):
        super().__init__(titulo, autor, isbn, duracion, 'Audiovisual')
        self.formato = formato

