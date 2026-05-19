archivo = open("usuarios.txt", "a")

while True:
    nombre = input("Introduce un nombre (o 'salir'): ")

    if nombre.lower() == "salir":
        break

    edad = input("Introduce la edad: ")

    archivo.write(f"{nombre} - {edad}\n")

archivo.close()

print("✅ Datos guardados correctamente")
