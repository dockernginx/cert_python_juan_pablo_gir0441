'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 /  /2022
Descripción: Esto es un programa que tomaremos los codijos de los dos ultimos ejercicios
pero con la diferencia es que trabajeromos con 3 argumentos  y debemos
regresa el dia correspondiente del año. 
'''
def isYearLeap(year): #en esta función vamos a verificar que el año sea del año gregoriano 
   if year < 1582: #En esta condicional vamos a verificar que el año sea actual al calendario gregoriano
    print("No entra en el calendario gregoriano")#Reciclamos el codjo del ejercicio lab4_3_1_6 para los años
   elif year % 4 !=0: 
    return False
   elif year % 100 != 0: 
     return True
   elif year % 400 != 0:
    return False
   else: 
    return True
def days_in_month(year, month):
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]#Recolectamos los meses con sus respectivos 
    if year(year) and month == 2 : #En esta sección hacemos una condicional para saber si el mes es par
          return 29
    return meses[month - 1] #en cuantos a los meses toma la posición menos 1

def dayOfYear(year, month, day):#en esta función sabremos el dia y año que 
    if year < 1582: #Verificamos el mes
        return None
    if month > 12 or month <1: #Que este dentro de los 12 meses
        return None
    if day > daysInMonth (year, month) or day < 1: #que el dia sea mayor al dia con el mes 
        return None
    total = day
    month = month - 1
    while month > 0: #Condionamos que el mes sea mayor a 0 
          total += daysInMonth(year, month)
          month-=1
    return total

print(dayOfYear(2000, 12, 31))