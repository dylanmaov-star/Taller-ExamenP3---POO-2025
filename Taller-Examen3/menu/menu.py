from modelos.modeloBaseDatos import BaseDatos
from modelos.modeloGallina import Gallina

def menu():
    base = BaseDatos()

    while True:
        print("\n=== MENÚ GRANJA AVÍCOLA ===")
        print("1. Registrar nueva gallina")
        print("2. Registrar produccion semanal")
        print("3. Consultar gallina")
        print("4. Actualizar datos de la gallina")
        print("5. Listar todas las gallinas")
        print("6. Eliminar gallina")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Codigo de la gallina: ")
            raza = input("Raza: ")
            edad = int(input("Edad (en meses): "))
            nueva = Gallina(codigo, raza, edad)
            base.agregarGallina(nueva)

        elif opcion == "2":
            codigo = input("Ingrese el codigo de la gallina: ")
            gallina = base.buscarGallina(codigo)
            if gallina:
                cantidad = int(input("Ingrese cantidad de huevos producidos esta semana: "))
                gallina.registrarProduccion(cantidad)
                print("Producción registrada correctamente")
            else:
                print("Gallina no encontrada")

        elif opcion == "3":
            codigo = input("Ingrese el codigo de la gallina: ")
            gallina = base.buscarGallina(codigo)
            if gallina:
                gallina.mostrarInfo()
            else:
                print("No se encontro el codigo de la gallina ingresada")

        elif opcion == "4":
            codigo = input("Ingrese el codigo de la gallina a actualizar: ")
            gallina = base.buscarGallina(codigo)
            if gallina:
                print("\n--- Deje en blanco si NO desea modificar el dato ---")
                nueva_raza = input(f"Nueva raza (actual: {gallina.raza}): ")
                nueva_edad = input(f"Nueva edad (actual: {gallina.edad}): ")
                base.actualizarGallina(codigo, nueva_raza, nueva_edad)
            else:
                print("Gallina no encontrada.")

        elif opcion == "5":
            base.listarGallinas()

        elif opcion == "6":
            codigo = input("Ingrese el codigo de la gallina a eliminar: ")
            base.eliminarGallina(codigo)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intente de nuevo")