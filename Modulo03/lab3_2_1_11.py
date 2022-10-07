'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  26 / sep /2022
Descripción: Esto es un programa que come vocales introduces cualquier palabra y te lo imprime sin 
las vocales pero aqui le declaramos las letras a una variable. 
'''
word_without_vowels = ""
user_word = input(('Ingresa una palabra: '))
# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = user_word.upper()
for letter in user_word:
  if letter == 'A': 
      continue
  elif letter == 'E':
      continue
  elif letter == 'I':
      continue
  elif letter == 'O':
      continue
  elif letter == 'U':
      continue
  else:
    word_without_vowels = letter
    print(word_without_vowels)
   # Completa el cuerpo del bucle.
   


# Imprimir la palabra asignada a word_without_vowels.
