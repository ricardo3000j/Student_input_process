# Student_input_process

## Stack del proyecto
- Python 3.10.11

## Requerimientos funcionales
## Requerimientos no funcionales
## Capacidad
## High Level
## Estructura del proyecto
`input.txt` - Archivo de entrada con informacion de estudiantes
`output.txt` - Reporte generado por la aplicacion al redireccionar stdout.
`main.py` - Entrypoint para ejecucion del proyecto

`data.py` - Estructura de datos que almacenara el input para simular BD

`src/data_wrangler.py` - Modulo para limpieza y transformacion de datos

`src/report_creation.py` - modulo para generar reporte de salida a partir de la data procesada  
`src/serializers/report_serializer.py` - Serializar reporte para generar output
`src/serializers/input_deserializer.py` - Modulo que procesara input.txt para convertirlo en la estructura de datos deseada

`src/models.py` Modulo que contiene modelado de los objectos que se utilizan en el proyecto, Entrada, Salida
`src/utils` - modulo con funciones compartidas de ayuda
`/tests` - modulo que contiene test suite en Pytest



## Code Standards
- Este proyecto utiliza Python `black` para formato de codigo, [Leer acerca de black formatter](https://black.readthedocs.io/en/stable/the_black_code_style/index.html)

## Razonamiento 


## Test cases
Input error handler:
-1 Empty line
-2 Solo comando
-3 sin comando
-3 missing student name
-4 wrong time format 
-5 Sin hora de entrada
-6 Sin hora de salida
-7 hora de entrada o salida con formato incorrecto
-7 hora de entrada o salida no es un formato de hora valida ()
- Nombre no valido


Output validation:
-Estudiante sin asistencias
-Estudiante sin registro
--8 Dia de la semana incorrecto
-7 Hora de Salida menor a hora de entrada