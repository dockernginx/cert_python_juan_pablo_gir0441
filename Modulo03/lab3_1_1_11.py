'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  26 / sep /2022
Descripción: Esto es un programa que calcula los impuestos dependiendo de cuanto gane 
por ejemplo si gana más de 85528 se le cobra más y sino menos pagara
'''
income = float(input("Introduce el ingreso anual: "))
tax = 0.0
if income < 85528  :
    tax = income * 0.18 - 556.02
if income > 85528 : 
    tax =  income * 0.32 - 14839.02 
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")