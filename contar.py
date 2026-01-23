import sys

if len(sys.argv) < 2:
    print()
    filename = input("Introduce el nombre completo del archivo--> ")
else:
    filename = sys.argv[1]

with open(f"{filename}","r", encoding='utf-8') as archivo:
    contenido = archivo.read()
    palabras = contenido.split()
    total_palabras = len(palabras)
print()
print(f"El archivo tiene un total de {total_palabras} palabras.")
print()