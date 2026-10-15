# Sistema de Catalogación de Libros Inteligente - Biblioteca PUCE

## Integrantes
- Luciana Aldás
- Francisco Narváez
- Anahí Real

## Problema
El procesamiento manual de material heterogéneo en la biblioteca (libros impresos, publicaciones periódicas, revistas, hemeroteca y tesis digitales o físicas) genera un procesamiento en el registro muy tardado, errores de categorización y dificultades en la asignación de ubicaciones físicas y en enlaces digitales.

## Usuario
Personal de catalogación de la biblioteaca, bibliotecarios y administradores del repositorio documental de la PUCE.

## Objetivo
Implementar un sistema en Python bajo Programación orientada a objetoss que agilice el registro, validación y consulta de recursos físicos y virtuales en la biblioteca.

## Alcance de la primera entrega
- Implementación de la jerarquía básica (`Recurso`, `LibroImpreso`, `RecursoDigital`) y el contenedor `SeccionBiblioteca` en un archivo funcional (`main.py`).
- Puesta en marcha de recursos físicos y digitales con validación básica de atributos.
- Ejecución por terminal que liste las fichas catalográficas generadas.

## Funcionalidades propuestas
1. Registro rápido de recursos clasificando automáticamente entre soporte físico y virtual.
2. Consulta de fichas bibliográficas (muestra estantería física o enlace digital según corresponda).
3. Búsqueda por título, autor o código de clasificación institucional.
4. Reporte básico de inventario.


## Clases iniciales

- **Recurso:** Define la información común de los recursos bibliográficos.
- **LibroImpreso:** Representa un libro físico con su información bibliográfica e ISBN.
- **RecursoDigital:** Representa un recurso digital con su formato de archivo.
- **RegistroAcceso:** Conserva la ubicación o enlace de acceso y el estado de disponibilidad de un recurso.
- **Bibliotecario:** Representa a la persona encargada de una sección de la biblioteca.
- **SeccionBiblioteca:** Reúne recursos bibliográficos y muestra su estado.

## Relaciones iniciales

- SeccionBiblioteca se asocia con Bibliotecario.
- SeccionBiblioteca agrega objetos Recurso.
- Recurso compone objetos RegistroAcceso.
- LibroImpreso es un tipo de Recurso.
- RecursoDigital es un tipo de Recurso.

## Ejecución

Abra esta carpeta en Visual Studio Code y ejecute:

```text
python main.py
````
