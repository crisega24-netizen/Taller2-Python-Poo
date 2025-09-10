class NumeroBase:
    def __init__(self, valor):
        self.valor = valor

    def descripcion(self):
        return str(self.valor)


class NumeroFizzBuzz(NumeroBase):
    def descripcion(self):
        if self.valor % 3 == 0 and self.valor % 5 == 0:
            return "FizzBuzz"
        elif self.valor % 3 == 0:
            return "Fizz"
        elif self.valor % 5 == 0:
            return "Buzz"
        else:
            return str(self.valor)


class Resultado:
    def __init__(self, numero, resultado):
        self.numero = numero
        self.resultado = resultado

    def mostrar(self):
        print(f"{self.numero} → {self.resultado}")


class SistemaFizzBuzz:
    def __init__(self):
        self.resultados = []  

    def mostrarBienvenida(self):
        print("\n===== Bienvenido al Juego FizzBuzz =====")
        print("Problema a resolver: Mostrar los números del 1 al 100 con las siguientes reglas:")
        print("- Múltiplos de 3 → Fizz")
        print("- Múltiplos de 5 → Buzz")
        print("- Múltiplos de 3 y 5 → FizzBuzz")

    def ejecutarFizzBuzz(self):
        self.resultados = []  
        for i in range(1, 101):
            numero = NumeroFizzBuzz(i)
            resultado = Resultado(i, numero.descripcion())
            self.resultados.append(resultado)
        print("Se ha ejecutado el FizzBuzz y guardado en la lista.")

    def mostrarResultados(self):
        if not self.resultados:
            print("No hay resultados aún. Ejecute primero el ejercicio.")
        else:
            for resultado in self.resultados:
                resultado.mostrar()

    def reiniciar(self):
        self.resultados = []
        print("Los resultados se han borrado. Lista reiniciada.")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\n======= Menú De Opciones ========")
            print("1. Ejecutar FizzBuzz")
            print("2. Ver resultados")
            print("3. Reiniciar resultados")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ejecutarFizzBuzz()
            elif opcion == "2":
                self.mostrarResultados()
            elif opcion == "3":
                self.reiniciar()
            elif opcion == "4":
                print("Saliendo del juego FizzBuzz. ¡Adiooooooooooooossssss!\n")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


# ============= Zona De Código Principal ============
sistema = SistemaFizzBuzz()
sistema.menu()