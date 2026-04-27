def aciertanumero(numero):
    if (numero == 4):
        mensaje = "¡enhorabuena! Has acertado el numero"
    elif (numero > 4):
        mensaje = "¡MEC ERROR! Te has equivocado de numero"
    else:
        mensaje = "¡MEC ERROR! Te sigues equivocando de numero"
    return mensaje

#Pedimos al usuario que adivine el numero
numero = float(input("Acierta el numero que estoy pensando: "))

#Llamamos acierta numero para que nos diga el mensaje
mensaje = aciertanumero (numero)
#imprimimos el mensaje con el resultado del numero elegido
print(mensaje)