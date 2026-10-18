from abc import ABC, abstractmethod

# 1. Clase Abstracta MandoDistancia
class MandoDistancia(ABC):
    
    @abstractmethod
    def encender(self):
        """Método abstracto para encender el dispositivo"""
        pass

    @abstractmethod
    def apagar(self):
        """Método abstracto para apagar el dispositivo"""
        pass

    @abstractmethod
    def cambiar_estado(self):
        """Método abstracto para cambiar el estado o modo del dispositivo"""
        pass


# 2. Clases Hijas

class TV(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.canal = 1

    def encender(self):
        self.encendido = True
        print("TV: Se ha encendido la televisión.")

    def apagar(self):
        self.encendido = False
        print("TV: Se ha apagado la televisión.")

    def cambiar_estado(self):
        if self.encendido:
            self.canal += 1
            print(f"TV: Canal cambiado al canal {self.canal}.")
        else:
            print("TV: No se puede cambiar de canal porque la TV está apagada.")


class ReproductorMusica(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.reproduciendo = False

    def encender(self):
        self.encendido = True
        print("ReproductorMusica: El reproductor está encendido.")

    def apagar(self):
        self.encendido = False
        self.reproduciendo = False
        print("ReproductorMusica: El reproductor se ha apagado.")

    def cambiar_estado(self):
        if self.encendido:
            self.reproduciendo = not self.reproduciendo
            estado = "Reproduciendo música" if self.reproduciendo else "En pausa"
            print(f"ReproductorMusica: Estado cambiado a -> {estado}")
        else:
            print("ReproductorMusica: Enciende el dispositivo primero.")


class Luces(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.intensidad = "Media"

    def encender(self):
        self.encendido = True
        print("Luces: Luces encendidas.")

    def apagar(self):
        self.encendido = False
        print("Luces: Luces apagadas.")

    def cambiar_estado(self):
        if self.encendido:
            intensidades = ["Baja", "Media", "Alta"]
            i = intensidades.index(self.intensidad)
            self.intensidad = intensidades[(i + 1) % len(intensidades)]
            print(f"Luces: Intensidad ajustada a {self.intensidad}.")
        else:
            print("Luces: Las luces están apagadas.")


class ControlTemperatura(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.temperatura = 22  # En grados Celsius

    def encender(self):
        self.encendido = True
        print("ControlTemperatura: Climatizador encendido.")

    def apagar(self):
        self.encendido = False
        print("ControlTemperatura: Climatizador apagado.")

    def cambiar_estado(self):
        if self.encendido:
            self.temperatura += 1
            print(f"ControlTemperatura: Temperatura ajustada a {self.temperatura}°C.")
        else:
            print("ControlTemperatura: Dispositivo apagado.")


class Rumba(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.modo = "Limpiando"

    def encender(self):
        self.encendido = True
        print("Rumba: Aspiradora Rumba encendida y comenzando limpieza.")

    def apagar(self):
        self.encendido = False
        print("Rumba: Aspiradora Rumba apagada y regresando a la base de carga.")

    def cambiar_estado(self):
        if self.encendido:
            self.modo = "Volviendo a la base" if self.modo == "Limpiando" else "Limpiando"
            print(f"Rumba: Estado cambiado a -> {self.modo}.")
        else:
            print("Rumba: La Rumba está apagada.")


# 3. Ejemplo de Uso / Prueba del Código
if __name__ == "__main__":
    dispositivos = [
        TV(),
        ReproductorMusica(),
        Luces(),
        ControlTemperatura(),
        Rumba()
    ]

    print("--- PROBANDO DISPOSITIVOS ---\n")
    for dispositivo in dispositivos:
        dispositivo.encender()
        dispositivo.cambiar_estado()
        dispositivo.apagar()
        print("-" * 30)