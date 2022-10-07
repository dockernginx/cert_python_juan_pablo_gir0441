'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  26 / sep /2022
Descripción: Esto es un programa de un mago que te hacer caer en un bucle que tienes que adivinar su 
numero magico y sino lo haces te quedas ahi pero sigues intentando su numero magico. 
'''


secret_number = 777
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int(input())
if(secret_number == number): 
    print("¡Bien hecho, muggle! Eres libre ahora!")
else: 
    while secret_number != number: 
     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
     break
     print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
