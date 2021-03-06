from funciones_xml import *

opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de libros
2. Número de libros por autor
3. Buscar libros por subcadena del argumento
4. Buscar libros por género
5. Comprar libro
6. Salir

Opción: '''))
while opcion<1 or opcion>6:
	print("Error. Introduce el número de la opción correcta.")
	opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de libros
2. Número de libros por autor
3. Buscar libros por subcadena del argumento
4. Buscar libros por género
5. Comprar libro
6. Salir

Opción: '''))
while opcion!=6:
	if opcion<1 or opcion>6:
		print("Error. Introduce el número de la opción correcta.")
		print()
	elif opcion==1:
		for libro in ListaLibros():
			print("Título: "+libro.get("titulo"))
			print("Año: "+libro.get("anio"))
			print("Género(s): ")
			for gen in libro.get("genero"):
				print(gen)
			print()
	elif opcion==2:
		for autor in ListaAutores():
			print("Nombre: "+autor.get("nombre")+" "+autor.get("apellido"))
			print("Sexo: "+autor.get("sexo"))
			print("Número de libros registrados: "+str(LibrosPorAutor()[ListaAutores().index(autor)]))
			print()
	elif opcion==3:
		sub=input("Introduce una subcadena: ")
		print()
		FiltroArgumento(sub)
	elif opcion==4:
		print("Lista de géneros registrados:")
		print()
		for gen in ListaGeneros():
			print(gen)
		print()
		genero=input("Introduce el nombre de un género de la lista anterior: ")
		FiltroGenero(genero)
	elif opcion==5:
		titulo=input("Introduce el título de un libro: ")
		print()
		InfoLibro(titulo)
		print()
		compra=input("¿Quieres comprar el libro? (s/n): ")
		print()
		if compra=="s":
			EnlaceCompra(titulo)
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