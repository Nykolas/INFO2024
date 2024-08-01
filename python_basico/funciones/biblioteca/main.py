from biblioteca import crear_libro, agregar_libro, buscar_libro, mostrar_catalogo

biblioteca_del_info = []

libro1 = crear_libro('Lógica de programación', 'Omar Iván Trejos Buriticá', 2017)
libro2 = crear_libro('Lógica de programación orientada a objetos', 'Efraín Oviedo Regino', 2015)

agregar_libro(biblioteca_del_info, libro1)
agregar_libro(biblioteca_del_info, libro2)

mostrar_catalogo(biblioteca_del_info)

libro_buscado = buscar_libro(biblioteca_del_info, 'Lógica de programación')
print(libro_buscado)
