import random
import datetime
import hashlib
import time

# Definir zonas y temperaturas por defecto
zonas = {
    'Sala': 20,
    'Cocina': 25,
    'Dormitorio': 20
}

# Definir horarios y temperaturas objetivo
horarios = {
    'Noche': {
        'Sala': 15,
        'Cocina': 10,
        'Dormitorio': 20
    }
}

# Función para ajustar la temperatura
def ajustar_temperatura(zona, temperatura):
    zonas[zona] = temperatura
    print(f"La temperatura en {zona} se ajustó a {temperatura}°C")

# Función para mostrar la temperatura actual en cada zona
def mostrar_temperaturas():
    print("Temperaturas actuales:")
    for zona, temperatura in zonas.items():
        print(f"{zona}: {temperatura}°C")

# Función para ajustar la temperatura automáticamente en función del horario
def ajustar_temperatura_automaticamente():
    horario_actual = datetime.datetime.now().strftime('%H:%M')
    for zona, temperatura in zonas.items():
        if horario_actual > '19:00' and zona in horarios['Noche']:
            temperatura_objetivo = horarios['Noche'][zona]
        else:
            temperatura_objetivo = temperatura
        
        nueva_temperatura = temperatura_objetivo + random.randint(-1, 1)
        zonas[zona] = nueva_temperatura
        if nueva_temperatura != temperatura:
            print(f"La temperatura en {zona} ha sido ajustada automáticamente a {nueva_temperatura}°C")

# Proceso principal
def main():
    MAX_INTENTOS = 3  # cantidad máxima de intentos permitidos
    BLOQUEO_TIEMPO = 60  # tiempo de bloqueo en segundos
    intentos = 0  # contador de intentos
    tiempo_bloqueo = None  # tiempo de inicio del bloqueo
    hash_correcto = hashlib.sha256('Diego123'.encode()).hexdigest()

    while True:
        print("\nGracias por elegir HSmart , bienvenido!")
        print("1. Configurar Zonas de Temperatura")
        print("2. Controlar Temperatura por Zonas")
        print("3. Temperaturas Actuales")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            print("Configuración de Zonas de Temperatura:")
            for zona in zonas.keys():
                temperatura = int(input(f"Ingresa la temperatura deseada para {zona}: "))
                ajustar_temperatura(zona, temperatura)

        elif opcion == '2':
            mostrar_temperaturas()
            zona = input("Selecciona la zona: ")
            if zona in zonas:
                temperatura = int(input("Ingresa la temperatura que quieres: "))
                ajustar_temperatura(zona, temperatura)
            else:
                print("Zona no disponible.")

        elif opcion == '3':
            mostrar_temperaturas()

        elif opcion == '4':
            print("¡Que tengas un buen día!")
            break

        else:
            print("Opción no válida. Por favor, seleccione de nuevo.")

        ajustar_temperatura_automaticamente()

        if tiempo_bloqueo and (time.time() - tiempo_bloqueo) < BLOQUEO_TIEMPO:
            print(f"Sistema bloqueado. Espera {int(BLOQUEO_TIEMPO - (time.time() - tiempo_bloqueo))} segundos.")
            continue
        else:
            tiempo_bloqueo = None

        password = input("Ingresa la contraseña: ")
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        if hash_password == hash_correcto:
            intentos = 0
        else:
            intentos += 1
            if intentos >= MAX_INTENTOS:
                print("Muchos intentos, se bloqueará el sistema")
                tiempo_bloqueo = time.time()
                intentos = 0
            else:
                print(f"Contraseña incorrecta. Te quedan {MAX_INTENTOS - intentos} intentos.")

if __name__ == "__main__":
    main()
