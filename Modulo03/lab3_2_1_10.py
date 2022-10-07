# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  26 / sep /2022
Descripción: Esto es un programa para comer las vocales colocas cualquier palabra pero al 
momenot de imprimir quita las vocales. 
'''
palabra = input(("Ingresa una palabra: "))
palabra = palabra.upper()
for letra in palabra:
    # Completa el cuerpo del bucle for.
   if letra == 'A': 
      continue
   elif letra == 'E':
      continue
   elif letra == 'I':
      continue
   elif letra == 'O':
      continue
   elif letra == 'U':
      continue
   else:
    print (letra)

    