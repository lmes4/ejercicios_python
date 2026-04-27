#Lista de meses del año
mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

#Pedimos numero al usuario
numero = int(input("Di un número del 1 al 12: "))

#Validar
if numero == 6:
    print("Junio, ¡el mejor mes!")
#Mostrar mes correspondiente
print(mes[numero - 1])
