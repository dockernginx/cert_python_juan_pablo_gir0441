income = float(input("Introduce el ingreso anual: "))
tax = 0.0
if income < 85528  :
    tax = income * 0.18 - 556.02
if income > 85528 : 
    tax =  income * 0.32 - 14839.02 
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")