#Pedir al usuario que introduzca dos numeros
#Convertimos a numero. int(sin decimales), float (puede tener decimales)
numero1 = float(input("Introduzca el precio de la camiseta"))
numero2 = float(input("Introduzca el precio de la sudadera"))
numero3 = float(input("Introduzca el precio de la gorra"))

#Hacemos las operaciones
#Calcula la suma total
suma = numero1 + numero2 + numero3
# Calcular IVA (21%)
iva = suma * 0.21
# Total con IVA
total = suma + iva

#Imprimimos los resultados
print("El total sin IVA es:", suma)
print("El IVA (21%) es:", iva)
print("El total con IVA incluido es:", total)
