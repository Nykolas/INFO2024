
class Libro():
    def __init__(self, titulo, autor, isbn, paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.genero = genero
        self.__prestado = False
    
    def esta_prestado(self):
        return self.__prestado

    def disponible(self):
        return not self.__prestado

    def prestar(self):
        self.__prestado = True

class Lector():
    def __init__(self, nombre, edad, direccion, numero_socio, tiene_permiso=True):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numero_socio = numero_socio
        self.__tiene_permiso = tiene_permiso 

    def tiene_permisos(self):
        return self.__tiene_permiso 
        
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
    
    def buscar_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        print(f"El libro no se encuentra en esta libreria")
    
    def prestar_libro(self,libro,lector):
        if libro.disponible():
            if lector.tiene_permisos():
                libro.prestar()
                print(f"se asigno el prestamo del libro {libro.titulo}")
            else:
                print(f"el lector {lector.nombre} no tiene permisos")
        else:
            print(f"el libro {libro.titulo} no esta disponible")


## MAIN ###
libreria1 = Libreria()

libro1 = Libro('autos','tesla',111,167,'autos')
lector1 = Lector('Nicolas',34,'calle siempre viva 123',1)

libreria1.agregar_lector(lector1)
libreria1.agregar_libro(libro1)


titulo = input("que libro quiere llevar: ")
libro_a_prestar = libreria1.buscar_libro(titulo)

libreria1.prestar_libro(libro_a_prestar, lector1)

libreria1.mostrar_libros()



