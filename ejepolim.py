import math

class Fraccion:
    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        # Calcula el máximo común divisor para simplificar la fracción
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd
        
        # Opcional: mantener el signo negativo en el numerador si el denominador es negativo
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

    def __add__(self, otro):
        if isinstance(otro, Fraccion):
            nuevo_numerador = (self.numerador * otro.denominador) + (otro.numerador * self.denominador)
            nuevo_denominador = self.denominador * otro.denominador
            return Fraccion(nuevo_numerador, nuevo_denominador)
        raise TypeError("El operador '+' solo está soportado entre objetos de la clase Fraccion.")

    def __sub__(self, otro):
        if isinstance(otro, Fraccion):
            nuevo_numerador = (self.numerador * otro.denominador) - (otro.numerador * self.denominador)
            nuevo_denominador = self.denominador * otro.denominador
            return Fraccion(nuevo_numerador, nuevo_denominador)
        raise TypeError("El operador '-' solo está soportado entre objetos de la clase Fraccion.")

    def __str__(self):
        # Presenta el resultado con el formato "numerador / denominador"
        return f"{self.numerador} / {self.denominador}"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    f1 = Fraccion(2, 4)  # Se simplificará automáticamente a 1 / 2
    f2 = Fraccion(1, 3)

    suma = f1 + f2
    resta = f1 - f2

    print(f"Fracción 1: {f1}")
    print(f"Fracción 2: {f2}")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")