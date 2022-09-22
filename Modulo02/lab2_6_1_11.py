'''
Nombre: Juan Pablo Palma Apoderado
Fecha: 22 / sep / 2022
Descripción: Tomara horas y minutos , y tiempo restante para que termine una determinada hora
'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
print("Hora: ", hour, mins, "Duarara: ", dura)
hour_res = (hour % 26)+ 1
min_res= mins % 60
print("Horas res: ", hour_res)
print("Minutos res: ", min_res)
# Escribe tu código aqui.59