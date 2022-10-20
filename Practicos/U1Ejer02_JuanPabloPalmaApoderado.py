'''
Nombre: Juan Pablo Palma Apoderado
Fecha: 13 / oct / 2022
Descripción: EL ejercicio 
'''
nom = ['Francisco', 'Pedro','Juan','Fernando'] #nombramos un  arreglo nom con los nombres de los amigos
print("El tamaño de la lista es: ", len(nom))#Imprimimos el tamaño del arreglo con la función len
print('El contenido de la lista es: ', nom)#Imprimimos todos los elementos del arreglo
nom.insert(1,'Joaquin') #Insertamos en la posición 1 a Joaquin y recorremos a Pedro una posición
nom.append('Luis Miguel')#Por ultimo agregamos comom ultimo elemento a LUIS MIGUEL
for nombres in nom:  #Imprimimos con un FOR losm elemntos de la lista un por uno
    print(nombres)