class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.prestado = False
        self.historial_prestamos = []

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.historial_prestamos = []

class Catalogo:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def libros_disponibles(self):
        return [libro for libro in self.libros if not libro.prestado]

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro.autor.lower()]

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.catalogo = Catalogo()
        self.prestamos = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        if libro in self.catalogo.libros and not libro.prestado:
            libro.prestado = True
            prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
            usuario.historial_prestamos.append(prestamo)
            libro.historial_prestamos.append(prestamo)
            self.prestamos.append(prestamo)

    def devolver_libro(self, libro, usuario, fecha_devolucion):
        for prestamo in usuario.historial_prestamos:
            if prestamo.libro == libro and prestamo.fecha_devolucion is None:
                libro.prestado = False
                prestamo.fecha_devolucion = fecha_devolucion
                break

    def prestamos_activos(self):
        return [prestamo for prestamo in self.prestamos if prestamo.fecha_devolucion is None]

    def historial_prestamos_libro(self, libro):
        return libro.historial_prestamos

# Crear instancias
biblioteca = Biblioteca()

# Agregar libros al catálogo
libro1 = Libro("Juanito y Simon", "VALENTIN", "+18")
libro2 = Libro("Valentin y las 8 enanas", "Nicolas", "Accion")
biblioteca.catalogo.agregar_libro(libro1)
biblioteca.catalogo.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan", "13456671")
usuario2 = Usuario("Maria Gonzalez", "209123413")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Realizar préstamos y devoluciones
fecha_prestamo = "2023-08-29"
fecha_devolucion = "2023-09-05"
biblioteca.prestar_libro(libro1, usuario1, fecha_prestamo, fecha_devolucion)
biblioteca.devolver_libro(libro1, usuario1, fecha_devolucion)

# Realizar búsquedas
libros_por_titulo = biblioteca.catalogo.buscar_por_titulo("Juanito y Simon")
libros_por_autor = biblioteca.catalogo.buscar_por_autor("Nicolas")

# Consultar préstamos activos
prestamos_activos = biblioteca.prestamos_activos()

# Consultar historial de préstamos por libro
historial_libro = biblioteca.historial_prestamos_libro(libro1)

# Mostrar resultados
print("Libros disponibles:")
for libro in biblioteca.catalogo.libros_disponibles():
    print(libro.titulo)

print("Préstamos activos:")
for prestamo in prestamos_activos:
    print(f"Libro: {prestamo.libro.titulo}, Usuario: {prestamo.usuario.nombre}")

print("Historial de préstamos del libro:")
for prestamo in historial_libro:
    print(f"Usuario: {prestamo.usuario.nombre}, Fecha de préstamo: {prestamo.fecha_prestamo}")
