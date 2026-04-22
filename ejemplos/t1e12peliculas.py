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


#Get values entered by the user
movie_name = input("What is your favorite movie? ")
director_name = input("Who is the director? ")
release_year = input("What year was it released? ")
genre_name = input("What genre is the movie? ")
duration_minutes = input("How long is the movie? ")


print("Your favorite movie is", movie_name)
print("The director of the movie is", director_name)
print("The release year was", release_year)
print("The genre of the movie is", genre_name)
print("The duration of the movie is", duration_minutes)
print("Has awards?", has_awards)