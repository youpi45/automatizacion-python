archivo = open("usuarios.txt", "a")

while True:
    nombre = input("Introduce un nombre (o 'salir'): ")

    if nombre.lower() == "salir":
        break

    archivo.write(nombre + "\n")

archivo.close()

print("✅ Datos guardados correctamente")
