import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None:

    print("He encontrado el texto")
else:
    print("No he encontrado el text")

textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())

print(len(re.findall(textoBuscar, cadena)))