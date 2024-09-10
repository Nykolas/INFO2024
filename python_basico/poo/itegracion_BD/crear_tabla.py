import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('data.db')
print("¡Conexión exitosa de base de datos!")

# Crear la tabla PERSONA
conn.execute('''
    CREATE TABLE PERSONA
    (ID INT PRIMARY KEY NOT NULL,
    NOMBRE TEXT NOT NULL,
    EDAD INT NOT NULL,
    DIRECCION CHAR(50));
''')
print("¡Tabla creada exitosamente!")

# Cerrar la conexión
conn.close()
