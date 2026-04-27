#Lista de planetas del Sistema Solar
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

#Pedimos numero al usuario
numero = int(input("Di un número del 1 al 8: "))

#Validar
if numero < 1 or numero > 8:
    print("Error, numero invalido")
else:
    print(planetas[numero - 1])