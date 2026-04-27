#Guardamos la ciudad del usuario
ciudad = input("Introduce tu ciudad: ")
#unimos 2 cadenas
origen = "Mi ciudad de origen es " + ciudad
#obtenemos el numero de letras de la cadena
longitud = len(origen)
#poner la cadena en mayusculas
origenmayusculas = origen.upper()
#poner la cadena en minusculas
origenminusculas = origen.lower()
#IMPRIMIR CADENAS
#imprimimos la palabra
print(origen)
#imprimir la longitud (al ser un numero no puede ir solo)
print("Longitud ", longitud)
#imprimir cadena en mayusculas
print(origenmayusculas)
#imprimir la cadena en minusculas
print(origenminusculas)