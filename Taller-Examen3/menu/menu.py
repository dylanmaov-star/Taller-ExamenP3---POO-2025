from modelos.modeloBaseDatos import BaseDatos
from modelos.modeloGallina import Gallina
def menu():
    base = BaseDatos()

    while True:
        print("\n=== MENÚ GRANJA AVÍCOLA ===")
        print("1. Registrar nueva gallina")
        print("2. Registrar produccion semanal")
        print("3. Consultar gallina")
        print("4. Listar todas las gallinas")
        print("5. Eliminar gallina")
        print("6. Salir")

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
            base.listarGallinas()

        elif opcion == "5":
            codigo = input("Ingrese el codigo de la gallina a eliminar: ")
            base.eliminarGallina(codigo)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida. Intente de nuevo")