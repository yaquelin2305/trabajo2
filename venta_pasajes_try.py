

totalingreso = 0

pasaje = int(input("Ingrese la cantidad de pasajes que desea vender:"))

for i in range(pasaje):

    while True:
        valor_pasaje = input(f"Ingresar valor del pasaje N°{i+1}: ")

        try:
            valor_pasaje = int(valor_pasaje)
            totalingreso += valor_pasaje
            break
        except ValueError:
            print("La entrada no es un número valido. Por favor vuelva a intentarlo.")

print(f"Total de ingresos por pasajes: {totalingreso}")


