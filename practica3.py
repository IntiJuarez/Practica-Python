import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor() #connection.execute() oficial, es un acceso directo no 
#estándar que crea un objeto de cursor intermedio


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


#TIPOS DE CONSULTAS:
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")

#UPDATE
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO = 'pelota'")

#DELETE
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

