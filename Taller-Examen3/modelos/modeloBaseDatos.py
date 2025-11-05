from modelos.modeloGallina import Gallina

class BaseDatos:
    def __init__(self):
        self.lista_gallinas = []

    def agregarGallina(self, gallina):
        self.lista_gallinas.append(gallina)
        print("Gallina registrada correctamente.")

    def buscarGallina(self, codigo):
        for g in self.lista_gallinas:
            if g.codigo == codigo:
                return g
        return None

    def listarGallinas(self):
        if self.lista_gallinas == []:
            print("No hay gallinas registradas")
            return
        print("\n--- LISTA DE GALLINAS ---")
        for g in self.lista_gallinas:
            print(f"Código: {g.codigo} | Raza: {g.raza} | Edad: {g.edad} meses | Total Huevos: {g.total_huevos}")

    def eliminarGallina(self, codigo):
        gallina = self.buscarGallina(codigo)
        if gallina:
            self.lista_gallinas.remove(gallina)
            print("Gallina eliminada correctamente.")
        else:
            print("No se encontró una gallina con ese código.")