'''
Nombre: Juan Pablo Palma Apoderado
Fecha: 13 / oct / 2022
'''
numeros_control = [1219100524,1219100537,1219100543,121910133,1219100484] #Agregamos un arrreglo con los numeros de control
nombre = [] #Otro arreglo con nombres vacio
aml= '' #Decalramos una varible de texto vacia 
for numcontrol in numeros_control: #Recorre el for de los numeros de control
    print("Ingresa el nombre con el No.Control ",numcontrol) #Toma cada numero de control
    aml = input() #agregamos su nombre
    nombre.append(aml)#Se va agregando el nombre en la posición de cada numero de control
print(nombre)#Imprime el arreglo agregado de los nombre de los alumnos
numerotemp = 0 #Declaramos una variable igual a 0 tomada como numero de control
while True: #Mientras es verdadero se ejecuta el codijo
    numerotemp = int(input("Ingresa el numero de control: "))#El usuario ingresear a la variable antes mencioanda el numero de control que quiere buscar
    if numeros_control == numeros_control:  #Verificammos en el arreglo de numeros_control es igual a que usuario desea buscar
        print('El numero de control si fue encontrado')#Mostrara si fue encontrado en el arreglo
    else: 
        print('El numero de control si fue encontrado')#Mostrara si no fue encontrado en el arreglo
    break