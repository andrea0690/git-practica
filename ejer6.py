#Crea un programa donde el usuario adivine un número entre 1 y 10.

import random

number = random.randint(1,10)


numero = int(input('Ingresa un numero del 1 al 10 '))
print(number)

if number == numero:
    print('Ganaste')
else:
    print('Perdiste')