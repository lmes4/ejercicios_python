#Cadena
nombre = "Pelicula favorita"
#Numeros (int)
año = 1997
#Numeros (int)
minutos = 104
#Booleanos (True o False)
tiene_premios = False

#Imprimir las variables
print("Nombre", nombre)
print("Año", año)
print("Minutos ", minutos)
print("Tiene premios?", tiene_premios)

#Obtener valores introducidos por el usuario

nombre_pelicula = input("Cual es tu pelicula favorita?")
nombre_director = input("Cual es el director?")
año_lanzamiento = input("En que año se estreno?")
nombre_genero = input("Que genero tiene la pelicula?")
minutos_duracion = input("Cuanto dura la pelicula?")
# Booleano
tiene_premios = input("¿Tiene premios? (si/no): ") == "no"


print("Tu pelicula favorita es ", nombre_pelicula)

print("El director de la pelicula es ", nombre_director)

print("El año de lanzamiento fue ", año_lanzamiento)

print("El genero de la pelicula es ", nombre_genero)

print("La duracion de la pelicula es ", minutos_duracion)

print("¿Tiene premios?", tiene_premios)