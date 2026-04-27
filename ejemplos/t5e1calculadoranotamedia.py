#Pedir al usuario cuantas notas quiere introducir
cantidad = int(input("¿Cuántas notas quieres introducir? "))

suma = 0

#Bucle para pedir cada nota
for i in range(cantidad):
    nota = float(input(f"Introduce la nota {i+1}: "))
    suma += nota

#Calcular la media
media = suma / cantidad

#Imprimimos suma y media
print(f"La suma total es: {suma}")
print(f"La media es: {media}")