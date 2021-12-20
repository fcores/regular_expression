import re

#cadena="Estoy trabajando con python en domingo y semana santa. El proximo domingo no voy a trabajar nada"


#print(re.search("sabado",cadena)) ##Buscar un string en particular

#busqueda="domingo"

#texto_encontrado=re.search(busqueda,cadena)

#print(texto_encontrado.start()) #Posicion inicial

#print(texto_encontrado.end()) #Posicion final

#print(texto_encontrado.span()) #Posicion inicial y final

#print(re.findall(busqueda,cadena)) #Me devuelve una lista con las veces que aparece una descripción

####Meta caracteres

lista_nombres=["Antonio Banderas","Facundo Cores","Armando Banquito","Facundo Arana","Julio Cores"]

for nombre in lista_nombres:
        if re.findall("^Facundo",nombre): ##Con el ^me devuelve todos los que arrancan con Facundo
                print(nombre)
        if re.findall("Cores$",nombre):
                print(nombre)
