import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor() #connection.execute() oficial, es un acceso directo no 
#estándar que crea un objeto de cursor intermedio

# miCursor.execute('''
#                  CREATE TABLE PRODUCTOS (
#                  CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#                  NOMBRE_ARTICULO VARCHAR(50),
#                  PRECIO INTEGER,
#                  SECCION VARCHAR(20))
#             ''')


# productos=[
    
#     ("AR01", "Pelota", 20, "Juguetería"),
#     ("AR02", "Pantalón", 15, "Confección"),
#     ("AR03", "Destornillador", 25, "Ferretería"),
#     ("AR04", "Jarrón", 45, "Cerámica")
# ]


#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

#Muestra de error al querer ingresar un dato con el mismo código de artículo.
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05', 'tren', 15, 'jugueteria')")


#Forma de creacar una primary key autoincremental

miCursor.execute('''

    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[
    ("Pelota", 20, "Juguetería"),
    (",Pantalón", 15, "Confección"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 45, "Cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


miConexion.commit()

miConexion.close()


