def crear_libro(titulo, autor, anio):
    return {'titulo': titulo, 'autor': autor, 'anio': anio}

def agregar_libro(biblioteca, libro):
    biblioteca.append(libro)

def buscar_libro(biblioteca, titulo):
    for libro in biblioteca:
        if libro['titulo'] == titulo:
            return libro
    return None

def mostrar_catalogo(biblioteca):
    for libro in biblioteca:
        print(f'Titulo: {libro["titulo"]}, Autor: {libro["autor"]}, Año: {libro["anio"]}')

def funcion_de_muestra():
    pass
