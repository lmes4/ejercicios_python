#Define los siguientes precios
camiseta = 10
sudadera = 28.5
gorra = 5.5

cantidad_camisetas = int(input("Cuantas camisetas quieres"))
cantidad_sudaderas = int(input("Cuantas sudaderas quieres"))
cantidad_gorras = int(input("Cuantas gorras quieres"))

#Hacemos las operaciones
precio_total_camisetas = cantidad_camisetas * camiseta
precio_total_sudaderas = cantidad_sudaderas * sudadera
precio_total_gorras = cantidad_gorras * gorra
#Calcula la suma total
precio_total_compra = precio_total_camisetas + precio_total_sudaderas + precio_total_gorras
#Calcular IVA (21%)
iva = precio_total_compra * 0.21
#Total con IVA
total = precio_total_compra + iva

#Imprimimos los resultados
print("El total sin IVA es:", precio_total_compra)
print("El IVA (21%) es:", iva)
print("El total con IVA incluido es:", total)
