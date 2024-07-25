
contacto_dicionario = {'nombre':'nicolas','edad':34,'telefono':3624252525}

#metodo diccionario para obtener los valores.
#print(contacto_dicionario.values())
#metodo diccionario para obtener tuplas con clave valor.
#print(contacto_dicionario.items())

#MOSTRAR CLAVE Y VALOR DE UN DICCIONARIO

#for k,v in contacto_dicionario.items():
#    print(f'clave {k}--> valor {v}')

#WHILE CONTINUE Y BREAK
'''
i = 0
while i<=10:
    if i == 3:
        break
    print(i)
    i = i + 1

print("TERMINO")
'''
i = 0
while i<=10:
    i = i + 1
    if i == 3:
        continue
    print(i)

print("TERMINO")
