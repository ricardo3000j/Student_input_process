# Student_input_process

## Stack del proyecto

- Python 3.10.11

## Instrucciones de ejecucion

- ejecutar aplicacion utilizar comando `python main.py input.txt`
- ejecutar suite de test utilizar comando `python -m unittest discover tests`

## Estructura del proyecto

- `input.txt` - Archivo de entrada con informacion de estudiantes
- `output.txt` - Reporte generado por la aplicacion al redireccionar stdout.
- `main.py` - Entrypoint para ejecucion del proyecto y donde se encuentra el main app()
- `/tests` - modulo que contiene test suite en unittest
- `/tests/unit_test` - modulo que contiene unit test de cada una de las funciones del proyecto
- `/tests/integration_test`-Modulo que contiene prueba de integracion de las operaciones principales del proyecto
- `/src`- Contiene todos los modulos, funciones y clases desarrollados para el proyecto
- `/src/utils` - modulo con funciones compartidas de ayuda
- `/src/models.py` Modulo que contiene modelado de los objectos que se utilizan en el proyecto, Entrada, Salida
- `/src/db.py`- Estructura de datos que almacenara el input para simular BD
- `/src/data_wrangler.py` - Modulo para limpieza, transformacion de datos, manipulacion de datos
- `/src/serializers` - Modulo para la deserializacion de la entrada input.txt y serializacion de reporte de asitencia
- `/src/student_input.py` - Clase para manejo de la entreda de datos y manejo hasta su insercion en el registro de datos
- `/src/ouput_report.py` - Objecto que contendra los reporte de asistencias y generara la salida del reporte.

## Code Standards

- Este proyecto utiliza Python `black` para formato de codigo, [Leer acerca de black formatter](https://black.readthedocs.io/en/stable/the_black_code_style/index.html)

## Razonamiento

- Se decidio realizar el diseño e implementacion de este proyecto siguiendo un flujo similar al de una aplicacion backend.
En el cual podemos diferenciar claramente dos etapas.
- Entrada de datos: Proceso donde se toma el parametro, se valida, serializa, filtra y se inserta en un registro.
- Salida de datos: se toman los datos del registro, se procesan y se genera a salida serializada.

- Se optado por no utlizar dependencias externas para facilitar la prueba de este proyecto, sin tener que configurar ningun entorno
- De igual manera no se hara integracion de otro servicio por la razon mencionada previamente. 

Se ha estructurado el codigo de forma que sea de bajo acoplamiento, mantenible y escalable. 

Acerca de las entradas y filtrado:
- Se consdera como entrada valida aquella que cuente con el comando Student o Presence
- En el caso del comando Student se considerara valida la entrada si tiene una longitud de al menos dos elementos.
- En el caso del comando Presence se considerara valida la entrada si tiene una longitud minima de al menos 5 elementos.
- El formato de hora utilizado sera HH:MM, entradas con otro formato de momento seran descartadas. 
- En el modelo de datos para las asistencias el unico campo opcional sera el código de la sala
pues no se utiliza en el calculo para la generacion del reporte. Sin embargo de llegarse a requerir para
generar otros reportes enfocados a las salas si debera ser requerido. 
- Los compos, Comando, nombre, dia de la semana, hora de entrada y salida, son requeridos de faltar alguno
se considera la entrada como invalida
- Un nombre se considera valido si es un string sin numeros, ni caracteres especiales
- Un dia de la semana es valida si su valor es entre 1 y 7
- Se considera entrada invalida si la hora de salida es menor a la hora de entrada

- Acerca de la entructura de datos:
la persistencia de los datos solo debe ser durante tiempo de ejecucion, no se contara con servicio de base de datos.
por lo que al terminar la ejecucion del programa se eliminaran.
- registro de estudiante (studet_registry) es un objecto, con patron singleton, que servira para almacenar cada una de las entradas y leerlas para generar el reporte.

- Se opto por el patro singleton de modo que en cada uno de los modulos tengan acceso a la misma instancia, garantizando asi la consistencia de los datos.

- Cuando se recibe el comando Student se crea un nuevo atributo en el registro
- Cuando se recibe el comando presence se busca el atributo en el registro y se inserta la asistencia.
- No se guardaran asistencia sin haber existido previamente el comando student que registre al estudiante. 


- se crearon modelos para guardar los records de asistencia en el registro para facilidad de manejo y tener una capa de atraccion para manejar los datos. 

- Se agrego el uso de logger, pues en arquitecturas distruidas y microservicios debe estar incluida para el monitoreo de la infraestructura y la ejecucion del servicio. 

- Se implemento algorithmo quick sort para ordenamiento de la salida serializada del reporte, este puede ser basado en cualquier atributo del objeto de record y se puede selevcionar si el ordamiento es ascendente o descendente. 

- La clase filter se agregar para agrupar todas las posibles validacions al realizarse en las entradas

## Test cases
- Basado en las consideraciones de una entrada valida se deben de tener en cuenta los siguientes test cases (incluidos edges cases)
para garantizar el correcto funcionamiento.

Entrada 
- 1 Empty line
- 2 Solo comando
- 3 Sin comando
- 4 Comando no valido
- 5 Sin Nombre de estudiante
- 6 Nombre de estudiante invalido
- 7 DIa de la semana incorrecto
- 8 Sin hora de entrada
- 8 Sin hora de salida
- 10 hora de entrada o salida con formato incorrecto
- 11 hora de entrada o salida no es un valor correcto
- 12 hora de entrada mayor a la de salida
- 14 solo hay entradas de registro (student)
- 15 solo hay entradas de asistencia (Presence)
- 16 Sin entradas validas, solo entradas invalidas

Para la generacion del reporte se consideran los siguientes test cases 
- Estudiante sin asistencias
- Estudiante sin registro
- Estudiante con solo una asitencia valida
- Periodo de asistencia menor a 5 minutos 
