import sqlite3

miConexion = sqlite3.connect("Primera Base")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, CATEGORIA VACHAR(50))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# variosProductos=[

#     ("Camiseta", 10, "Deportes"),
#     ("Jarrón", 90, "Cerámica"),
#     ("Camión", 20, "Juguetería")
# ]


#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall() #devuelve lista de elementos

#print(variosProductos)

for productos in variosProductos:

    print("Nombre Artículo: ", productos[0], " Sección: ", productos[2])


miConexion.commit()


miConexion.close()
