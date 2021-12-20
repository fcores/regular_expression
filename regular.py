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

#lista_nombres=["Antonio Banderas","Facundo Cores","Armando Banquito","Facundo Arana","Julio Cores"]

#for nombre in lista_nombres:
#        if re.findall("^Facundo",nombre): ##Con el ^me devuelve todos los que arrancan con Facundo
#                print(nombre)
#        if re.findall("Cores$",nombre): ##Con el $ me devuelve todos los que terminan con Cores
#                print(nombre)

#lista_terminos=["camión","camion","niños","niñas","ejemplo"]

#for terminos in lista_terminos:
#        if re.findall("cami[oó]",terminos): ##Con el [] puedo poner las opciones de caracteres que pueden estar en el texto
#                print(terminos)
#        if re.findall("niñ[oa]",terminos): 
#                print(terminos)

#for terminos in lista_terminos:
       # if re.findall("[p-z]",terminos): ##Con el [] en este ejemplo me devuelve las palabras que contienen letras entre la p y z
        #         print(terminos)
        # if re.findall("^[a-f]",terminos): ##Con el [] en este ejemplo me devuelve las palabras que empiezan con alguna letra entre la a y la f
        #         print(terminos)
#        if re.findall("[l-p]$",terminos): ##Con el [] en este ejemplo me devuelve las palabras que terminan con alguna letra entre la l y la p
#                print(terminos)

# lista_terminos=["Ma1","Se1","Ma2","Va1","Ba1","Se1","Ma3","Ma4"]

# for termino in lista_terminos:
#         # if re.findall("Ma[1-3]",termino): #Aca luego del Ma pongo el [] y las opciones, fijate que no me trae el Ma4 
#         #         print(termino)
                
# for termino in lista_terminos:
#         if re.findall("Ma[^1-3]",termino): #Aca luego del Ma pongo el [] y las opciones, fijate que con ^ niego el rango
#                 print(termino)

#lista_terminos=["Ma1","Se1","Ma2","Va1","Ba1","Se2","Ma3","Ma4","Se3","SeA","SeB","Va2","SeC"]

# for termino in lista_terminos:
#         if re.findall("Se[0-2A-B]",termino): #Aca luego del Ma pongo el [] y las opciones, fijate que busca entre 0 y 2 y entre A y B
#                 print(termino)


####Funcion MATH

nombre1="Carmen Lopez"
nombre2="Juan Diaz"
nombre3="Sandra Martin"

if re.match(".andra",nombre3,re.IGNORECASE): #Match busca en al principio y necesita 3 parametros el tercero opcional, search busca en todo el texto
        print("Encontre la persona")
else:
        print("No la encontre")
