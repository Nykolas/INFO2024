import sqlite3

conn = sqlite3.connect('data.db')

# Insertar datos en la tabla PERSONA
conn.execute("INSERT INTO PERSONA (ID, NOMBRE, EDAD, DIRECCION) \
              VALUES (1, 'Pablo', 32, 'Av. Chaco 123')")

conn.execute("INSERT INTO PERSONA (ID, NOMBRE, EDAD, DIRECCION) \
              VALUES (2, 'Ana', 25, 'Av. Nueva 123')")

# Confirmar los cambios en la base de datos
conn.commit()
print("¡Registros guardados exitosamente!")

conn.close()
