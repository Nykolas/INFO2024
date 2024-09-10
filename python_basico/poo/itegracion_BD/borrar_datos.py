import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('data.db')

conn.execute("DELETE from PERSONA where id = 2")
conn.commit()
# Consultar datos de la tabla PERSONA
cursor = conn.execute("SELECT id, nombre, direccion FROM PERSONA")

print(cursor)
# Recorrer y mostrar los resultados
for row in cursor:
    print("ID = ", row[0])
    print("NOMBRE = ", row[1])
    print("DIRECCION = ", row[2], "\n")

conn.close()