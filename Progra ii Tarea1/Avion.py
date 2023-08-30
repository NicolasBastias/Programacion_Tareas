class Avion:
    def __init__(self, modelo, num_asientos):
        self.modelo = modelo
        self.num_asientos = num_asientos

class Reservacion:
    def __init__(self, pasajero, vuelo):
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = "reservado"

    def cancelar(self):
        self.estado = "cancelado"

class Pasajero:
    def __init__(self, nombre, num_pasaporte):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.reservaciones = []

    def reservar_vuelo(self, reservacion):
        self.reservaciones.append(reservacion)

    def ver_reservaciones(self):
        return [reservacion.vuelo.num_vuelo for reservacion in self.reservaciones]
    
class Vuelo:
    def __init__(self, num_vuelo, origen, destino, fecha_hora, avion_asignado):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avion_asignado = avion_asignado
        self.reservaciones = []

    def consultar_disponibilidad(self):
        return self.avion_asignado.num_asientos - len(self.reservaciones)

    def reservar_vuelo(self, pasajero):
        if self.consultar_disponibilidad() > 0 and pasajero not in self.reservaciones:
            reservacion = Reservacion(pasajero, self)
            self.reservaciones.append(reservacion)
            pasajero.reservar_vuelo(reservacion)
            return f"Se agendo una reservacion para {pasajero.nombre} en vuelo {self.num_vuelo}\n"
        elif pasajero in self.reservaciones:
            return f"{pasajero.nombre} ya tiene una reservación en el vuelo.\n"
        else:
            return "Lo sentimos, el vuelo está lleno."

    def cancelar_reservacion(self, pasajero):
        for reservacion in self.reservaciones:
            if reservacion.pasajero == pasajero:
                reservacion.cancelar()
                self.reservaciones.remove(reservacion)
                return f"Reservación cancelada para {pasajero.nombre} en vuelo {self.num_vuelo}\n"
        return f"No se encontró la reservación de {pasajero.nombre} en este vuelo.\n"

    def ver_pasajeros(self):
        return [reservacion.pasajero.nombre for reservacion in self.reservaciones]





# Ejemplo de uso del sistema:
avion1 = Avion("Boeing 737", 100)
avion2 = Avion("Airbus A320", 200)

vuelo1 = Vuelo("V123", "Nueva York", "Los Ángeles", "2023-08-31 14:00", avion1)
vuelo2 = Vuelo("V456", "Chicago", "Miami", "2023-09-05 10:30", avion2)

pasajero1 = Pasajero("Juan Perez", "ABC123")
pasajero2 = Pasajero("Maria Gomez", "XYZ789")
pasajero3 = Pasajero("Cualquier cosa", "XYZ789")

# Consultar disponibilidad de asientos
print("Asientos disponibles en vuelo 1:", vuelo1.consultar_disponibilidad())

# Reservar asientos
print(vuelo1.reservar_vuelo(pasajero1))
print(vuelo1.reservar_vuelo(pasajero2))



# Ver las reservaciones de un pasajero
print("Reservaciones de Juan Perez:", pasajero1.ver_reservaciones(),"\n")

# Ver la lista de pasajeros en un vuelo
print("Pasajeros en vuelo 1:", vuelo1.ver_pasajeros(),"\n")


# Cancelar una reservación
print(vuelo1.cancelar_reservacion(pasajero1))
print(vuelo1.cancelar_reservacion(pasajero3))

# Intentar reservar el mismo vuelo nuevamente
print(vuelo1.reservar_vuelo(pasajero1))

# Mostrar el estado de la reservación cancelada
print("Estado de la reservación:", vuelo1.reservaciones[0].estado,"\n")

print("Asientos disponibles en vuelo 1:", vuelo1.consultar_disponibilidad())

