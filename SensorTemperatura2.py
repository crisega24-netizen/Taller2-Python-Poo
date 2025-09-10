class ControlBase:
    def accion(self):
        return "Estado desconocido"


class Calefactor(ControlBase):
    def accion(self):
        return "Calefactor Encendido"


class Ventilador(ControlBase):
    def accion(self):
        return "Ventilador Encendido"


class Inactivo(ControlBase):
    def accion(self):
        return "Sistema Inactivo"


class Lectura:
    def __init__(self, temperatura, estado):
        self.temperatura = temperatura
        self.estado = estado

    def mostrar(self):
        print(f"{self.temperatura}°C → {self.estado}")


class SistemaInvernadero:
    def __init__(self):
        self.historial = []  

    def mostrarBienvenida(self):
        print("\n===== Bienvenido Al Sistema De Control de Temperatura =====")
        print("Problema a resolver: Simular el control de un invernadero")
        print("- Si la temperatura < 10°C → Calefactor Encendido")
        print("- Si la temperatura entre 10°C y 25°C → Sistema Inactivo")
        print("- Si la temperatura > 25°C → Ventilador Encendido")

    def leerNumero(self, mensaje):
        while True:
            entrada = input(mensaje)
            try:
                return float(entrada)
            except ValueError:
                print("Error: Debe ingresar un número válido.")

    def controlarTemperatura(self, temperatura):
        if temperatura < 10:
            dispositivo = Calefactor()
        elif temperatura > 25:
            dispositivo = Ventilador()
        else:
            dispositivo = Inactivo()

        estado = dispositivo.accion()
        lectura = Lectura(temperatura, estado)
        self.historial.append(lectura)
        print(f"Lectura registrada: {temperatura}°C → {estado}")

    def mostrarHistorial(self):
        if not self.historial:
            print("No hay lecturas registradas aún.")
        else:
            print("\nHistorial de lecturas:")
            for lectura in self.historial:
                lectura.mostrar()

    def reiniciar(self):
        self.historial = []
        print("El historial de lecturas ha sido borrado.")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\n======== Menú De Opciones =========")
            print("1. Ingresar temperatura y verificar estado")
            print("2. Ver historial de lecturas")
            print("3. Reiniciar historial")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                temperatura = self.leerNumero("Ingrese la temperatura en °C: ")
                self.controlarTemperatura(temperatura)
            elif opcion == "2":
                self.mostrarHistorial()
            elif opcion == "3":
                self.reiniciar()
            elif opcion == "4":
                print("Saliendo del sistema. ¡Adioooooooooooossssss!\n")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


# ============== Zona De Código principal ===========
sistema = SistemaInvernadero()
sistema.menu()