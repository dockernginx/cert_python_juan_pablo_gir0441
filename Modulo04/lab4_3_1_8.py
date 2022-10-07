'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 /  /2022
Descripción: Esto es un programa que tomaremos los codijos de los dos ultimos ejercicios
pero con la diferencia es que trabajeromos con 3 argumentos  y debemos
regresa el dia correspondiente del año. 
'''
def isYearLeap(year):
  if year % 100 !=0: 
    return False
  else: 
    return True

def days_in_month(year, month):
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year(year) and month == 2 : 
          return 29
    return meses[month - 1]

def dayOfYear(year, month, day):
    if year < 1582: 
        return None
    if month > 12 or month <1: 
        return None
    if day > daysInMonth (year, month) or dya < 1: 
        return None
    total = day
    month = month - 1
    while month > 0: 
          total += daysInMonth(year, month)
          month-=1
    return total

print(dayOfYear(2000, 12, 31))