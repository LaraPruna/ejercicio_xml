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
	for elem in libros:
		if sub in elem.xpath("./argument/text()")[0]:
			print("Titulo: "+elem.xpath("./@title")[0])
			print("Autor: "+elem.xpath("../@first")[0]+" "+elem.xpath("../@last")[0])
			print()

