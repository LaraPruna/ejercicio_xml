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
