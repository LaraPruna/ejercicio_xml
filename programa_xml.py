from funciones_xml import *

opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de libros
2. Número de libros por autor
3. Buscar libros por subcadena del argumento
4. Buscar libros por género
5. Comprar libro
6. Salir

Opción: '''))
while opcion!=6:
	if opcion==1:
		for libro in ListaLibros():
			print("Título: "+libro.get("titulo"))
			print("Año: "+libro.get("anio"))
			print("Género(s): ")
			for gen in libro.get("genero"):
				print(gen)
			print()
	opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de libros
2. Número de libros por autor
3. Buscar libros por subcadena del argumento
4. Buscar libros por género
5. Comprar libro
6. Salir

Opción: '''))

print("Fin del programa")