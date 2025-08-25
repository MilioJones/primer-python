#Programa que calcula la edad en el año 2100 usando la fecha actual

from datetime import datetime

#pedir datos al usuario
nombre = input("¿Cómo te llamas? ")
año_nacimiento = int(input("¿En qué año naciste? "))

#calcular edad actual
año_actual = datetime.now().year
edad = año_actual - año_nacimiento

#Calcular edad en el año 2100
año_2100 = 2100
edad_2100 = edad + (año_2100 - 2025)

#mostrar resultados
print(f"Hola {nombre}, tienes {edad} años.")
print(f"En el año {año_2100} tendrás {edad_2100} años.")
