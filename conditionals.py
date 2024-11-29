'''edad = 17

nombre = 'ale'

if edad < 18 or nombre != 'ale':
    print('No puedes pasar')
else:
    print('Bienvenido')'''
    
numero1 = int(input('ingresa el primer numero '))
numero2 = int(input('ingresa el segundo numero '))
numero3 = int(input('ingresa el tercer numero '))

if numero1 > numero2 and numero1>numero3:
    print(f"El numero mayor es {numero1}")
elif numero2 >numero1 and numero2> numero3:
    print(f"El numero mayor es el numero {numero2}")
else:
    print(f"El numero mayor es el numero {numero3}")