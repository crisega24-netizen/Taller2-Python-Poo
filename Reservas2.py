class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def descripcion(self):
        return f"{self.nombre}"


class Reserva:
    def __init__(self, persona, asiento):
        self.persona = persona
        self.asiento = asiento

    def mostrar(self):
        print(f"Asiento {self.asiento} reservado por {self.persona.descripcion()}")


class Sala:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.reservas = []  

    def verificarDisponibilidad(self):
        return len(self.reservas) < self.capacidad

    def agregarReserva(self, reserva):
        if self.verificarDisponibilidad():
            self.reservas.append(reserva)
            return True
        else:
            return False

    def mostrarReservas(self):
        if not self.reservas:
            print("No hay reservas realizadas aún.")
        else:
            for reserva in self.reservas:
                reserva.mostrar()

    def reiniciar(self):
        self.reservas = []  
        print("El sistema está reiniciado.")


class SistemaReservas:
    def __init__(self):
        self.sala = Sala(15)  

    def mostrarBienvenida(self):
        print("\n======== Bienvenido al Sistema de Reservas =========")
        print("Problema a resolver: Reserva de asientos en una sala de cine.")
        print("La sala tiene una capacidad limitada y se usarán LISTAS para almacenar las reservas.")

    def hacerReserva(self):
        if not self.sala.verificarDisponibilidad():
            print("No hay asientos disponibles.")
            return

        nombre = input("Ingrese el nombre de la persona que reserva: ")
        persona = Persona(nombre)

        asiento = len(self.sala.reservas) + 1
        reserva = Reserva(persona, asiento)

        if self.sala.agregarReserva(reserva):
            print("Reserva realizada con éxito.")
        else:
            print("No se pudo realizar la reserva.")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\nMenú de opciones:")
            print("1. Hacer una reserva")
            print("2. Ver reservas realizadas")
            print("3. Reiniciar el sistema de reservas")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.hacerReserva()
            elif opcion == "2":
                self.sala.mostrarReservas()
            elif opcion == "3":
                self.sala.reiniciar()
            elif opcion == "4":
                print("Saliendo del sistema. ¡Adiooooooooooossssssss!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


# =================== Zona De Código Principal ===================
sistema = SistemaReservas()
sistema.menu()
