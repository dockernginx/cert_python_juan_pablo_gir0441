'''
Nombre: Juan Pablo Palma Apoderado
Fecha: 13 / oct / 2022
Descripción: EL ejercicio No.1 Es crear una lista y dicha lista insertaremos un nuevo elemento en un posición 
especifica y otro con la función happend, por ultimo mostraremos los elemntos de la lista. Asi como mostrar la lista y el tamaño. 
'''
nom = ['Francisco', 'Pedro','Juan','Fernando'] #nombramos un  arreglo nom con los nombres de los amigos
print("El tamaño de la lista es: ", len(nom))#Imprimimos el tamaño del arreglo con la función len
print('El contenido de la lista es: ', nom)#Imprimimos todos los elementos del arreglo
nom.insert(1,'Joaquin') #Insertamos en la posición 1 a Joaquin y recorremos a Pedro una posición
nom.append('Luis Miguel')#Por ultimo agregamos comom ultimo elemento a LUIS MIGUEL
for nombres in nom:  #Imprimimos con un FOR losm elemntos de la lista un por uno
    print(nombres)