'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 / oct /2022
Descripción: Esto es un programa que nos da cuantro años muy distintos entre ellos pero tenemos que verificar que sea bsiiestos 
paar que nos muestre la leyenda OK o sino FALLIDO, nos da una lista con los resultado ya previstos solo es verificar que esten 
correctos los años. 
'''
def is_year_leap(year):
    
#
# Escribe tu código aquí.
#
  if year < 1582: #En esta condicional vamos a verificar que el año sea actual al calendario gregoriano
    print("No entra en el calendario gregoriano")
  elif year % 4 !=0: 
    return False
  elif year % 100 != 0: 
     return True
  elif year % 400 != 0:
    return False
  else: 
    return True
test_data = [1900, 2000, 2016, 1987] #Los años estan guardados los años que vamos a comparar
test_results = [False, True, True, False] #La posición de los años que deben regresar
for i in range(len(test_data)): #Recorre los años con el FOR
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]: #Si el resultado es igual a los test_result
		print("OK")
	else:
		print("Fallido")