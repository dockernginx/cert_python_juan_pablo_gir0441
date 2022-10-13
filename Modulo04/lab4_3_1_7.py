'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 / oct /2022
Descripción: Esto es un programa para realizar los comandos básicos de python
'''
def is_year_leap(year):
#
# Tu código del LABORATORIO 4.3.6.
#
  if year < 1582: 
    print("No entra en el calendario gregoriano")
  elif year % 4 !=0: 
    return False
  elif year % 100 != 0: 
     return True
  elif year % 400 != 0:
    return False
  else: 
    return True
def days_in_month(year, month): #Regresara el dia y mes 
    meses = [31,28,31,30,31,30,31,31,30,31,30,31] #Recolectaremos los meses en un  arreglo
    if is_year_leap(year) and month == 2 : #Rerificamos que tome el año y el mes se divisible entre dos 
          return 29
    return meses[month - 1]#Toma los meses del arreglo y toma otro mes para restarle uno , 
#
# Escribe tu código aquí.
#

test_years = [1900, 2000, 2016, 1987] #recolectamo los años en un arreglo 
test_months = [2, 2, 1, 11] #Recolectamos los meses en un arreglo
test_results = [28, 29, 31, 30] #Recolectamos los dias en un arreglo
for i in range(len(test_years)): #recorremos los años desde i 
	yr = test_years[i] #el año ddel arreglo lo asiganomos a la variable yr
	mo = test_months[i] #el mes que esta en el arreglo lo asginmos a la variable mo
	print(yr, mo, "->", end="") 
	result = days_in_month(yr, mo)#Asiganmos el dia del mes al alas variables que declaramos
	if result == test_results[i]:#el dia del mes lo asignamos al variable result
		print("OK")
	else:
		print("Fallido")
