from abc import ABC, abstractmethod

# 1. CLASE ABSTRACTA (PLANTILLA PRINCIPAL)
# Definimos MandoDistancia heredando de ABC (Abstract Base Class).
# Sirve como contrato: obliga a que cualquier dispositivo inteligente que herede de esta clase implemente obligatoriamente los métodos abstractos.
class MandoDistancia(ABC):
    
    @abstractmethod
    def encender(self):
        """Método abstracto: cada dispositivo debe definir cómo se enciende."""
        pass

    @abstractmethod
    def apagar(self):
        """Método abstracto: cada dispositivo debe definir cómo se apaga."""
        pass

    @abstractmethod
    def cambiar_estado(self):
        """Método abstracto: cada dispositivo define cómo cambia de modo, canal, etc."""
        pass

# 2. CLASES HIJAS (DISPOSITIVOS INTELIGENTES)

# Dispositivo 1: TV 
class TV(MandoDistancia):
    def __init__(self):
        self.encendido = False  # Estado inicial: apagada
        self.canal = 1          # Canal inicial

    def encender(self):
        self.encendido = True
        print("TV: Se ha encendido la televisión.")

    def apagar(self):
        self.encendido = False
        print("TV: Se ha apagado la televisión.")

    def cambiar_estado(self):
        # Cambia de canal solo si la televisión está encendida
        if self.encendido:
            self.canal += 1
            print(f"TV: Canal cambiado al canal {self.canal}.")
        else:
            print("TV: No se puede cambiar de canal porque la TV está apagada.")


# Dispositivo 2: Reproductor de Música 
class ReproductorMusica(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.reproduciendo = False  # Controla si suena música o está en pausa

    def encender(self):
        self.encendido = True
        print("ReproductorMusica: El reproductor está encendido.")

    def apagar(self):
        self.encendido = False
        self.reproduciendo = False
        print("ReproductorMusica: El reproductor se ha apagado.")

    def cambiar_estado(self):
        # Alterna entre reproducir y pausar si está encendido
        if self.encendido:
            self.reproduciendo = not self.reproduciendo
            estado = "Reproduciendo música" if self.reproduciendo else "En pausa"
            print(f"ReproductorMusica: Estado cambiado a -> {estado}")
        else:
            print("ReproductorMusica: Enciende el dispositivo primero.")


#Dispositivo 3: Luces
class Luces(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.intensidad = "Media"  # Nivel de brillo inicial

    def encender(self):
        self.encendido = True
        print("Luces: Luces encendidas.")

    def apagar(self):
        self.encendido = False
        print("Luces: Luces apagadas.")

    def cambiar_estado(self):
        # Rota entre las intensidades de las luces si están encendidas
        if self.encendido:
            intensidades = ["Baja", "Media", "Alta"]
            i = intensidades.index(self.intensidad)
            self.intensidad = intensidades[(i + 1) % len(intensidades)]
            print(f"Luces: Intensidad ajustada a {self.intensidad}.")
        else:
            print("Luces: Las luces están apagadas.")


#Dispositivo 4: Control de Temperatura
class ControlTemperatura(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.temperatura = 22  # Temperatura inicial en grados Celsius

    def encender(self):
        self.encendido = True
        print("ControlTemperatura: Climatizador encendido.")

    def apagar(self):
        self.encendido = False
        print("ControlTemperatura: Climatizador apagado.")

    def cambiar_estado(self):
        # Sube un grado la temperatura si está encendido
        if self.encendido:
            self.temperatura += 1
            print(f"ControlTemperatura: Temperatura ajustada a {self.temperatura}°C.")
        else:
            print("ControlTemperatura: Dispositivo apagado.")


#Dispositivo 5: Aspiradora Rumba
class Rumba(MandoDistancia):
    def __init__(self):
        self.encendido = False
        self.modo = "Limpiando"  # Modo de operación inicial

    def encender(self):
        self.encendido = True
        print("Rumba: Aspiradora Rumba encendida y comenzando limpieza.")

    def apagar(self):
        self.encendido = False
        print("Rumba: Aspiradora Rumba apagada y regresando a la base de carga.")

    def cambiar_estado(self):
        # Alterna el modo de trabajo de la Rumba si está encendida
        if self.encendido:
            self.modo = "Volviendo a la base" if self.modo == "Limpiando" else "Limpiando"
            print(f"Rumba: Estado cambiado a -> {self.modo}.")
        else:
            print("Rumba: La Rumba está apagada.")


# 3. EJEMPLO DE USO Y PRUEBAS

if __name__ == "__main__":
    # Creamos una lista que contiene objetos de cada dispositivo inteligente
    dispositivos = [
        TV(),
        ReproductorMusica(),
        Luces(),
        ControlTemperatura(),
        Rumba()
    ]

    print("--- PROBANDO DISPOSITIVOS ---\n")
    
    # Recorremos cada dispositivo aplicando polimorfismo: 
    # todos responden a las mismas llamadas gracias a la clase abstracta.
    for dispositivo in dispositivos:
        dispositivo.encender()       # Enciende el dispositivo actual
        dispositivo.cambiar_estado() # Cambia su estado/modo particular
        dispositivo.apagar()         # Apaga el dispositivo
        print("-" * 30)