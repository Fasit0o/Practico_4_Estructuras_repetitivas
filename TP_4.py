#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
numero_abs = abs(numero)
cantidad_digitos = len(str(numero_abs))
print("El número tiene", cantidad_digitos, "dígitos.")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1 

suma = 0

for i in range(num1 + 1, num2):
    suma += i  

print("La suma de los números comprendidos entre", num1, "y", num2, "es:", suma)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
num = 1
while num != 0:
    num = int(input("Ingrese un número entero: "))
    suma += num

print("El total acumulado es:", suma)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num = random.randint(0, 9)
intentos = 0

while num != int(input("Ingrese un número: ")):
    intentos += 1
    num = random.randint(0, 9)

print("El número era", num, "y tus intentos fueron", intentos)

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(0, 101):
    pares = i % 2
    print(pares)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i 

print("La suma de los números desde 0 hasta", n, "es:", suma)


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador = 0
contador_par = 0
contador_impar = 0
contador_negativo = 0
contador_positivo = 0

while contador < 100:
    numero = int(input("Ingrese un número entero: "))
    contador += 1
    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

    if numero < 0:
        contador_negativo += 1
    else:
        contador_positivo += 1

print("Números pares:", contador_par)
print("Números impares:", contador_impar)
print("Números negativos:", contador_negativo)
print("Números positivos:", contador_positivo)


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).


cantidad = 100 
suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero  

media = suma / cantidad

print("La media de los números ingresados es:", media)


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Ingrese un número entero: "))

signo = -1 if numero < 0 else 1

numero_str = str(abs(numero))

numero_invertido_str = numero_str[::-1]

numero_invertido = int(numero_invertido_str) * signo

print("El número invertido es:", numero_invertido)
