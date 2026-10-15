"""PRIMERA ENTREGA.

Esta versión utiliza únicamente contenidos estudiados hasta herencia básica.
Todavía no incluye sobrescritura, polimorfismo, módulos ni pruebas formales.
"""


class RegistroAcceso:
    """Conserva el estado de disponibilidad y la ubicación o enlace de acceso."""

    def __init__(self, ubicacion, disponible=True):
        self.ubicacion = ubicacion
        self.disponible = disponible

    def descripcion(self):
        estado = "Disponible" if self.disponible else "Prestado / No disponible"
        return f"[{estado}] Ubicación/Acceso: {self.ubicacion}"


class Recurso:
    """Clase base con la información común de los recursos de la biblioteca."""

    def __init__(self, codigo, titulo, autor, anio, soporte):
        # Encapsulación: protegemos los datos con guion bajo.
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._soporte = soporte

        # Composición: el recurso administra sus registros o copias creadas dentro.
        self._registros = []

    @property
    def titulo(self):
        return self._titulo

    @property
    def soporte(self):
        return self._soporte

    @property
    def codigo(self):
        return self._codigo

    def registrar_copia(self, ubicacion, disponible=True):
        # El RegistroAcceso se crea dentro del Recurso (Composición).
        nuevo_registro = RegistroAcceso(ubicacion, disponible)
        self._registros.append(nuevo_registro)

    def ultimo_registro(self):
        if len(self._registros) == 0:
            return None
        return self._registros[-1]


class LibroImpreso(Recurso):
    """Herencia: LibroImpreso es un tipo de Recurso con soporte Físico."""

    def __init__(self, codigo, titulo, autor, anio, isbn):
        # La clase base inicializa código, título, autor, año, soporte y registros.
        super().__init__(codigo, titulo, autor, anio, "Físico")
        self.isbn = isbn


class RecursoDigital(Recurso):
    """Herencia: RecursoDigital es un tipo de Recurso con soporte Digital."""

    def __init__(self, codigo, titulo, autor, anio, formato):
        super().__init__(codigo, titulo, autor, anio, "Digital")
        self.formato = formato


class Bibliotecario:
    """Persona encargada de supervisar o catalogar una sección."""

    def __init__(self, nombre):
        self.nombre = nombre


class SeccionBiblioteca:
    """Reúne recursos que fueron creados fuera de la sección."""

    def __init__(self, nombre):
        self.nombre = nombre
        self._recursos = []
        self._bibliotecario = None

    def asignar_bibliotecario(self, bibliotecario):
        # Asociación: los dos objetos existen por separado.
        self._bibliotecario = bibliotecario

    def agregar_recurso(self, recurso):
        # Agregación: recibimos un objeto Recurso ya creado.
        self._recursos.append(recurso)

    def mostrar_estado(self):
        print("Sección Biblioteca PUCE:", self.nombre)
        if self._bibliotecario is not None:
            print("Catalogador a cargo:", self._bibliotecario.nombre)

        for recurso in self._recursos:
            registro = recurso.ultimo_registro()
            if registro is None:
                print("-", recurso.titulo, f"({recurso.soporte}) sin registros")
            else:
                print("-", recurso.titulo, f"({recurso.soporte}) ->", registro.descripcion())


# Los objetos independientes se crean fuera de la sección.
catalogador = Bibliotecario("Ana Torres")
libro_fisico = LibroImpreso("LIB-01", "Estructuras de Datos en Python", "Mark Weiss", 2020, "978-013409")
tesis_digital = RecursoDigital("TES-01", "Minería de Texto en Repositorios PUCE", "Carlos Mora", 2024, "PDF")
seccion = SeccionBiblioteca("Ciencias Exactas e Ingeniería")

# Formamos las relaciones entre los objetos.
seccion.asignar_bibliotecario(catalogador)
seccion.agregar_recurso(libro_fisico)
seccion.agregar_recurso(tesis_digital)

# Registramos datos de ejemplo (Composición en acción).
libro_fisico.registrar_copia("Estantería Central - Piso 2", disponible=True)
tesis_digital.registrar_copia("https://repositorio.puce.edu.ec/handle/22000/123", disponible=True)

# Mostramos una evidencia de que la primera versión funciona.
seccion.mostrar_estado()