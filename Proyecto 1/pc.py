# Estaciones y rutas
estaciones = {
    51: "Estación Javier",
    61: "Estación Trébol",
    71: "Estación Don Bosco",
    82: "Estación Plaza Municipal"
}

rutas = [
    (51, 61, 39),
    (51, 71, 18),
    (71, 82, 23),
    (61, 51, 8),
    (82, 51, 42)
]

# Reportes
boletos_vendidos = {}
ingresos = 0

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Ver estaciones y rutas")
    print("2. Comprar boleto")
    print("3. Reportes")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("\nEstaciones:")
        for codigo, nombre in estaciones.items():
            print(f"{codigo}: {nombre}")

        print("\nRutas disponibles:")
        for origen, destino, distancia in rutas:
            print(f"{estaciones[origen]} -> {estaciones[destino]}, Distancia: {distancia} km")

    elif opcion == "2":
        while True:
            origen = int(input("\nIngrese el código de la estación de partida: "))
            if origen not in estaciones:
                print("Código de estación inválido. Intente nuevamente.")
                continue

            destino = int(input("Ingrese el código de la estación de destino: "))
            if destino not in estaciones:
                print("Código de estación inválido. Intente nuevamente.")
                continue

            ruta_encontrada = False
            for ruta in rutas:
                if (origen, destino) == (ruta[0], ruta[1]):
                    distancia = ruta[2]
                    ruta_encontrada = True
                    break

            if not ruta_encontrada:
                print("La ruta ingresada no existe. Intente nuevamente.")
                continue

            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            embarazada = input("¿Está embarazada? (si/no): ").lower() == "si" 

            precio = 1.5 * 8
            if distancia > 8:
                precio += (distancia - 8) * 0.25

            if 15 <= edad <= 25:
                precio *= 0.75

            if embarazada:
                precio = 0

            tiempo = distancia / 20

            print(f"\nEstación de partida: {estaciones[origen]}")
            print(f"Estación de destino: {estaciones[destino]}")
            print(f"Precio del boleto: Q{precio:.2f}")
            print(f"Tiempo estimado de viaje: {tiempo:.2f} horas")

            ruta = (origen, destino)
            if ruta not in boletos_vendidos:
                boletos_vendidos[ruta] = 0
            boletos_vendidos[ruta] += 1
            ingresos += precio

            break

    elif opcion == "3":
        print("\nReportes:")
        print("Boletos vendidos por ruta:")
        for ruta, cantidad in boletos_vendidos.items():
            origen, destino = ruta
            print(f"{estaciones[origen]} -> {estaciones[destino]}: {cantidad}")

        total_boletos = sum(boletos_vendidos.values())
        print(f"\nTotal de boletos vendidos: {total_boletos}")
        print(f"Total de ingresos: Q{ingresos:.2f}")

    elif opcion == "4":
        print("¡Que le vaya bien!")
        break

    else:
        print("Opción inválida.")