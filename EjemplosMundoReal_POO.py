# ---------------------------------------------
# Sistema de Reservas de Hotel (Ejemplo POO)
# ---------------------------------------------

# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # Ej: Simple, Doble, Suite
        self.precio = precio
        self.disponible = True  # Todas las habitaciones inician libres

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        """Vuelve a marcar la habitación como disponible."""
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} | {self.tipo} | ${self.precio} | {estado}"


# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} (CI: {self.cedula})"


# Clase que gestiona las reservas del hotel
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        """Calcula el costo total de la estadía."""
        return self.habitacion.precio * self.dias

    def __str__(self):
        return (f"Reserva:\n"
                f"  Cliente: {self.cliente}\n"
                f"  Habitación: {self.habitacion.numero} ({self.habitacion.tipo})\n"
                f"  Días: {self.dias}\n"
                f"  Total: ${self.calcular_total()}")


# Clase principal del hotel que administra habitaciones y reservas
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print("\n--- Lista de Habitaciones ---")
        for h in self.habitaciones:
            print(h)

    def reservar_habitacion(self, cliente, tipo, dias):
        """Busca una habitación disponible según el tipo y realiza la reserva."""
        for h in self.habitaciones:
            if h.tipo == tipo and h.disponible:
                if h.reservar():
                    reserva = Reserva(cliente, h, dias)
                    self.reservas.append(reserva)
                    return reserva
        return None


# ---------------------------
# Ejecución del programa
# ---------------------------
if __name__ == "__main__":
    # Crear hotel
    hotel = Hotel("Hotel Python Palace")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "Simple", 25))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 40))
    hotel.agregar_habitacion(Habitacion(201, "Suite", 100))

    # Mostrar habitaciones
    hotel.mostrar_habitaciones()

    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", "1234567890")

    # Reservar habitación
    reserva = hotel.reservar_habitacion(cliente1, "Doble", 3)

    if reserva:
        print("\nReserva realizada con éxito:")
        print(reserva)
    else:
        print("\nNo hay habitaciones disponibles del tipo solicitado.")
