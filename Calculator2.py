class OperacionBase:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular(self):
        pass  


class Suma(OperacionBase):
    def calcular(self):
        return self.num1 + self.num2


class Resta(OperacionBase):
    def calcular(self):
        return self.num1 - self.num2


class Multiplicacion(OperacionBase):
    def calcular(self):
        return self.num1 * self.num2


class Division(OperacionBase):
    def calcular(self):
        if self.num2 == 0:
            return "Error: División entre 0"
        return self.num1 / self.num2


class Operacion:
    def __init__(self, num1, num2, tipo, resultado):
        self.num1 = num1
        self.num2 = num2
        self.tipo = tipo
        self.resultado = resultado

    def mostrar(self):
        print(f"{self.num1} {self.tipo} {self.num2} = {self.resultado}")


class SistemaCalculadora:
    def __init__(self):
        self.historial = []  

    def mostrarBienvenida(self):
        print("\n======== Bienvenido a la Calculadora Pro MAX =======")
        print("Problema a resolver: Realizar operaciones básicas entre dos números.")
        print("Operaciones: suma, resta, multiplicación y división.")

    def leerNumero(self, mensaje):
        while True:
            entrada = input(mensaje)
            try:
                return float(entrada)
            except ValueError:
                print("Error: Debe ingresar un número válido (entero o decimal).")

    def realizarOperacion(self):
        num1 = self.leerNumero("Ingrese el primer número: ")
        num2 = self.leerNumero("Ingrese el segundo número: ")

        while True:
            print("\nOperaciones disponibles:")
            print("1. Suma (+)")
            print("2. Resta (-)")
            print("3. Multiplicación (*)")
            print("4. División (/)")
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                op = Suma(num1, num2)
                simbolo = "+"
            elif opcion == "2":
                op = Resta(num1, num2)
                simbolo = "-"
            elif opcion == "3":
                op = Multiplicacion(num1, num2)
                simbolo = "*"
            elif opcion == "4":
                op = Division(num1, num2)
                simbolo = "/"
            else:
                print("Opción inválida. Intente de nuevo.")
                continue

            resultado = op.calcular()
            operacion = Operacion(num1, num2, simbolo, resultado)
            self.historial.append(operacion)
            print("Operación realizada con éxito.")
            operacion.mostrar()
            break

    def mostrarHistorial(self):
        if not self.historial:
            print("No hay operaciones registradas aún.")
        else:
            print("\nHistorial de operaciones:")
            for op in self.historial:
                op.mostrar()

    def reiniciar(self):
        self.historial = []
        print("El historial de operaciones ha sido borrado.")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\n====== Menú De Opciones =======")
            print("1. Realizar un cálculo")
            print("2. Ver historial")
            print("3. Reiniciar historial")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.realizarOperacion()
            elif opcion == "2":
                self.mostrarHistorial()
            elif opcion == "3":
                self.reiniciar()
            elif opcion == "4":
                print("Saliendo de la calculadora. ¡Adioooooooooossssssss!\n")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


# ============ Zona De Código principal =============
sistema = SistemaCalculadora()
sistema.menu()