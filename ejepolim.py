import math

class Fraccion:
    # Inicializo los atributos de la fracción y la simplifico automáticamente al crear el objeto
    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        # Calculo el máximo común divisor (MCD) para simplificar la fracción
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd
        
        # Opcional: mantengo el signo negativo en el numerador si el denominador es negativo
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

    # Sobrecargo el operador '+' para sumar dos fracciones (Polimorfismo)
    def __add__(self, otro):
        if isinstance(otro, Fraccion):
            # Calculo el nuevo numerador aplicando la suma de fracciones con distinto denominador
            nuevo_numerador = (self.numerador * otro.denominador) + (otro.numerador * self.denominador)
            # Multiplico los denominadores para obtener el denominador común
            nuevo_denominador = self.denominador * otro.denominador
            # Retorno un nuevo objeto Fraccion (que se simplificará solo en su __init__)
            return Fraccion(nuevo_numerador, nuevo_denominador)
        raise TypeError("El operador '+' solo está soportado entre objetos de la clase Fraccion.")

    # Sobrecargo el operador '-' para restar dos fracciones (Polimorfismo)
    def __sub__(self, otro):
        if isinstance(otro, Fraccion):
            # Calculo el nuevo numerador aplicando la resta de fracciones
            nuevo_numerador = (self.numerador * otro.denominador) - (otro.numerador * self.denominador)
            # Multiplico los denominadores
            nuevo_denominador = self.denominador * otro.denominador
            # Retorno el objeto Fraccion resultante
            return Fraccion(nuevo_numerador, nuevo_denominador)
        raise TypeError("El operador '-' solo está soportado entre objetos de la clase Fraccion.")

    # Formateo la salida para que se imprima exactamente como "numerador / denominador"
    def __str__(self):
        return f"{self.numerador} / {self.denominador}"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Creo dos fracciones de prueba
    f1 = Fraccion(2, 4)  # Se simplificará automáticamente a 1 / 2
    f2 = Fraccion(1, 3)

    # Realizo las operaciones usando los operadores sobrecargados (+) y (-)
    suma = f1 + f2
    resta = f1 - f2

    # Imprimo los resultados por pantalla
    print(f"Fracción 1: {f1}")
    print(f"Fracción 2: {f2}")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")