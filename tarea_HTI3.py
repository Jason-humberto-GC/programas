import re
carpeta_nombre = "documentos\\"
archivo_nombre = "dos.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

expresion_regular=re.compile(r"(la)?(cual)? deriva?") 
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))
    
    
expresion_regular=re.compile(r"\d+(,\d+)*(\.\d+)?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))