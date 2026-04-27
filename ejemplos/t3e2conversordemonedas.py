#Pedimos a la usuaria la cantidad en euros
euros = float(input("Introduce una cantidad en euros: "))

#Convertimos a dolares
def convertiradolares(euros):
    dolares = euros * 1.1
    return dolares

#Convertimos a libras
def convertiralibras(euros):
    libras = euros * 0.87
    return libras

#Conversiones
dolares = convertiradolares(euros)
libras = convertiralibras(euros)

#CorreccionReyes
#Ask the user for an amount in euros
def conversor ():
    quantity_in_euros = float(input("Enter a quantity price in euros: "))

    print("Convert to Dollars")
    quantity_in_dollars = convert_from_euros_to_dolars(quantity_in_euros)
    print(quantity_in_dollars)

    print("Convert to Pound")
    print(convert_from_euros_to_pounds(quantity_in_euros))



conversor()