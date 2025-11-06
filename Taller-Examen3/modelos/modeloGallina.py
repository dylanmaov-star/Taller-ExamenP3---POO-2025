class Gallina:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.huevos_semana = 0 
        self.total_huevos = 0   

    def registrarProduccion(self, cantidad):
        self.huevos_semana = cantidad
        self.total_huevos += cantidad


    def actualizarDatos(self, nueva_raza=None, nueva_edad=None):
        if nueva_raza is not None and nueva_raza != "":
            self.raza = nueva_raza

        if nueva_edad is not None and nueva_edad != "":
            if nueva_edad.isdigit():
                self.edad = int(nueva_edad)
        else:
            print("La edad ingresada no es válida. No se actualizó.")

    
    
    def mostrarInfo(self):
        print(f"\nCódigo: {self.codigo}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} meses")
        print(f"Huevos esta semana: {self.huevos_semana}")
        print(f"Total acumulado: {self.total_huevos}")