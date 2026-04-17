#Obtener valores introducidos por el usuario

nombre_cancion = input("Cual es tu cancion favorita?")
nombre_artista = input("Quien la canta?")
nombre_album = input("Como se llama el album?")
año_lanzamiento = input("En que año se lanzo?")
segundos_duracion = input("Cuanto segundos dura la cancion?")
# Booleano
tiene_videoclip = input("¿Tiene videoclip? (si/no): ") == "si"


print("Tu cancion favorita es ", nombre_cancion)

print("La cancion la canta ", nombre_artista)

print("El album se llama ", nombre_album)

print("El año de lanzamiento fue ", año_lanzamiento)

print("La cancion dura ", segundos_duracion)

print("¿Tiene videoclip?", tiene_videoclip)