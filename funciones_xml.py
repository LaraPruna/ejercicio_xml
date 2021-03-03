from lxml import etree

def LeerXML():
	doc=etree.parse('libreria.xml')
	return doc

def ListaLibros():
	libros=LeerXML().xpath("/authors/author/book")
	lista=[]
	for elem in libros:
		libro={}
		libro["titulo"]=elem.xpath("./@title")[0]
		libro["anio"]=elem.xpath("./published/text()")[0]
		libro["genero"]=elem.xpath(".//genre/text()")
		lista.append(libro)
	return lista

def ListaAutores():
	autores=LeerXML().xpath("/authors/author")
	lista=[]
	for elem in autores:
		autor={}
		autor["nombre"]=elem.xpath("./@first")[0]
		autor["apellido"]=elem.xpath("./@last")[0]
		autor["sexo"]=elem.xpath("./@gender")[0]
		lista.append(autor)
	return lista

def LibrosPorAutor():
	autores=LeerXML().xpath("/authors/author")
	lista=[]
	for elem in autores:
		lista.append(len(elem.xpath("./book")))
	return lista

def FiltroArgumento(sub):
	libros=LeerXML().xpath("/authors/author/book")
	ind=True
	for elem in libros:
		if sub in elem.xpath("./argument/text()")[0]:
			print("Titulo: "+elem.xpath("./@title")[0])
			print("Autor: "+elem.xpath("../@first")[0]+" "+elem.xpath("../@last")[0])
			print()
			ind=False
	if ind:
		print("Esa subcadena no aparece en el argumento de ninguno de los libros registrados.")

def ListaGeneros():
	generos=LeerXML().xpath("/authors/author/book/genre/text()")
	lista=[]
	for gen in generos:
		if gen not in lista:
			lista.append(gen)
	return lista

def FiltroGenero(genero):
	libros=LeerXML().xpath("/authors/author/book")
	ind=True
	for lib in libros:
		if genero in lib.xpath("./genre/text()"):
			print("Titulo: "+lib.xpath("./@title")[0])
			print("Autor: "+lib.xpath("../@first")[0]+" "+lib.xpath("../@last")[0])
			print()
			ind=False
	if ind:
		print("No tenemos registrado ningún género con ese nombre.")
		print()

def InfoLibro(titulo):
	libros=LeerXML().xpath("/authors/author/book")
	ind=True
	for lib in libros:
		if titulo==lib.xpath("./@title")[0]:
			print("Autor: "+lib.xpath("../@first")[0]+" "+lib.xpath("../@last")[0])
			print("Generos:")
			for gen in lib.xpath("./genre/text()"):
				print(gen)
			print("Argumento: "+lib.xpath("./argument/text()")[0])
			ind=False
	if ind:
		print("Ese título no se encuentra registrada en nuestra librería.")

def EnlaceCompra(titulo):
	libros=LeerXML().xpath("/authors/author/book")
	for lib in libros:
		if titulo==lib.xpath("./@title")[0]:
			print("Enlace de compra: "+lib.xpath("./url/text()")[0])