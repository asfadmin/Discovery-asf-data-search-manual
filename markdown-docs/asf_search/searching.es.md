# Búsqueda

Cada función de búsqueda devuelve un objeto ```ASFSearchResults```:

- ```busqueda_geo()``` Encuentre información del producto sobre un área de interés usando una cadena WKT
- ```busqueda_granulo()``` Encuentre información del producto usando una lista de nombres de escenas
- ```busqueda_producto()``` Encuentre información del producto usando una lista de IDs de productos
- ```pila_desde_id()``` Encuentre una pila base de productos usando un ID de escena de referencia
- Si los enfoques de búsqueda anteriores no satisfacen sus necesidades, ```buscar()``` soporta todas las palabras clave disponibles:
    - ```buscar()``` Encuentre información del producto usando cualquier combinación de parámetros de búsqueda. Consulta la lista de palabras clave a continuación.

    - Ejemplos de algunos flujos de trabajo de búsqueda se pueden encontrar en este [script de muestra](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/hello_world.py). También puedes consultar los [cuadernos Jupyter](https://github.com/asfadmin/Discovery-asf_search/tree/master/examples) para flujos de trabajo de ejemplo.

Para un uso más avanzado, consulta las secciones [Clase ASFSearchResults](/asf_search/ASFSearchResults/) y [Clase ASFProduct](/asf_search/ASFProduct).

## Palabras clave

Las palabras clave se utilizan para encontrar los datos deseados. Usa tantas o tan pocas palabras clave como necesites. A continuación, se enumeran las palabras clave disponibles y sus descripciones. Además, se proporcionan numerosas constantes para facilitar el proceso de búsqueda. Actualmente, proporcionamos constantes para el modo de haz, dirección de vuelo, instrumento, plataforma, polarización y tipo de producto. Puedes ver la lista completa de [constantes aquí](https://github.com/asfadmin/Discovery-asf_search/tree/master/asf_search/constants).

### Parámetros del conjunto de datos
- <span style="color: #236192; font-size: 20px;">plataforma</span>
    - Consulta la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/PLATFORM.py)
    - Plataforma de teledetección remota que adquirió los datos. Sentinel-1 y ERS tienen múltiples plataformas de teledetección remota, y puede elegir si deseas especificar una plataforma específica. puede especificar un solo valor o una lista de valores.
    - También puede obtener la lista de constantes disponibles utilizando ```help(asf_search.constants.PLATFORM)```
    - Ejemplo:
        - plataforma=asf.PLATFORM.SENTINEL1A

- <span style="color: #236192; font-size: 20px;">instrumento</span>
    - Consulta la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/INSTRUMENT.py)
    - Instrumento de teledetección remota que adquirió los datos. Para algunas plataformas, como ALOS, hay varios instrumentos para elegir.
    - También puede obtener la lista de constantes disponibles utilizando ```help(asf_search.constants.INSTRUMENT)```
    - Ejemplo:
        - instrumento=asf.INSTRUMENT.AVNIR_2

- <span style="color: #236192; font-size: 20px;">absoluteBurstID</span>
    - Utilizado para los [productos de ráfaga](/datasets/using_ASF_data/#sentinel-1-bursts) de Sentinel-1. Cada valor identifica el conjunto de una ráfaga, representando todos los productos generados durante una subfranja específica. puede especificar un solo valor o una lista de valores. 
    - Ejemplo:
        - valor único: absoluteBurstID='102563902'
        - lista de valores: absoluteBurstID=['102563902', '103558145']

- <span style="color: #236192; font-size: 20px; font-size: 20px;">absoluteOrbit</span>
    - Para ALOS, ERS-1, ERS-2, JERS-1, RADARSAT-1, Sentinel-1A y Sentinel-1B, este valor corresponde al recuento de órbitas dentro del ciclo orbital. Para UAVSAR, es el [ID de vuelo](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.34282209.1335434931.1620087198-1930115146.1605056035). puede especificar un solo valor, un rango de valores o una lista de valores.
    - Ejemplo:
        - valor único: absoluteOrbit=25436
        - rango de valores: absoluteOrbit=(12005, 12008)
        - lista de valores: absoluteOrbit=[25436, 25450]  

- <span style="color: #236192; font-size: 20px;">asfFrame</span>
    - Ver también 'frame'
    - Esto es principalmente una referencia de marco de ASF / [JAXA](https://global.jaxa.jp/). Sin embargo, algunas plataformas utilizan otras convenciones. puede especificar un solo valor, un rango de valores o una lista de valores.
    - Ejemplo:
        - valor único: asfFrame=300
        - rango de valores: asfFrame=(2845, 2855)
        - lista de valores: asfFrame=[2800, 2845]
    - Valores:
        - ERS, JERS, RADARSAT: Marcos ASF de 0 a 900
        - ALOS PALSAR: Marcos JAXA de 0 a 7200
        - SEASAT: Marcos similares a ESA de 208 a 3458
        - Sentinel-1: Valores internos de 0 a 1184

- <span style="color: #236192; font-size: 20px;">beamMode</span>
    - Consulta la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/BEAMMODE.py)
    - El modo de haz utilizado para adquirir los datos.
    - También puede obtener la lista disponible de constantes utilizando ```help(asf_search.constants.BEAMMODE)```
    - Ejemplo:
        - beamMode=asf.BEAMMODE.POL

- <span style="color: #236192; font-size: 20px;">beamSwath</span>
    - La franja del haz abarca un ángulo de visión y un modo de haz. puede especificar un solo valor o una lista de valores.
    - Ejemplo:
        - valor único: beamSwath='IW'
        - lista de valores: beamSwath=['IW','EW']

- <span style="color: #236192; font-size: 20px;">campaign</span>
    - Solo para conjuntos de datos de UAVSAR, AIRSAR y Sentinel-1 Interferogram. Busca por el nombre de la campaña. puede especificar un solo valor.
    - Para obtener una lista de campañas disponibles, utiliza la función ```asf_search.campaigns()```. Debe proporcionar la plataforma deseada.
        - ```asf_search.campaigns(asf_search.PLATFORM.UAVSAR)```
    - Ejemplo:
        - campaign='Volcán Puracé, Colombia'

- <span style="color: #236192; font-size: 20px;">maxDoppler</span>
    - El Doppler proporciona una indicación de cuánto se desvía la dirección de observación de la dirección de vuelo ideal perpendicular.
    - Ejemplo:
        - maxDoppler=1500 o maxDoppler=1500.5

- <span style="color: #236192; font-size: 20px;">minDoppler</span>
    - El Doppler proporciona una indicación de cuánto se desvía la dirección de observación de la dirección de vuelo ideal perpendicular.
    - Ejemplo:
        - minDoppler=100 o minDoppler=1500.5

- <span style="color: #236192; font-size: 20px;">maxFaradayRotation</span>
    - La rotación del plano de polarización de la señal de radar afecta la imaginería. Las señales HH y HV se mezclan. Las rotaciones unidireccionales que exceden los 5° pueden reducir significativamente la precisión de la recuperación de parámetros geofísicos, como la biomasa forestal.
    - Ejemplo:
        - maxFaradayRotation=3.5

- <span style="color: #236192; font-size: 20px;">minFaradayRotation</span>
    - La rotación del plano de polarización de la señal de radar afecta la imaginería. Las señales HH y HV se mezclan. Las rotaciones unidireccionales que exceden los 5° pueden reducir significativamente la precisión de la recuperación de parámetros geofísicos, como la biomasa forestal.
    - Ejemplo:
        - minFaradayRotation=2

- <span style="color: #236192; font-size: 20px;">flightDirection</span>
    - Consulta la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/FLIGHT_DIRECTION.py)
    - Dirección de órbita del satélite durante la adquisición de datos. puede especificar un solo valor.
    - También puede obtener la lista disponible de constantes utilizando ```help(asf_search.constants.FLIGHT_DIRECTION)```
    - Ejemplo:
        - flightDirection=asf.FLIGHT_DIRECTION.ASCENDING

- <span style="color: #236192; font-size: 20px;">flightLine</span>
    - Especifica una línea de vuelo para UAVSAR o AIRSAR. puede especificar un solo valor.
    - Ejemplo:
        - UAVSAR: flightLine='05901'
        - AIRSAR: flightLine='gilmorecreek045-1.93044'

- <span style="color: #236192; font-size: 20px;">frame</span>
    - Consulta también 'asfFrame'
    - Los marcos referenciados por la ESA se ofrecen para brindar a los usuarios una convención de marcos universal. A cada marco de la ESA se le asigna un marco ASF correspondiente. puede especificar un solo valor, un rango de valores o una lista de valores.
    - Ejemplo:
        - valor único: frame=300
        - rango de valores: frame=(305, 315)
        - lista de valores: frame=[300, 303, 305]
    - Valores:
        - Cualquier número del 0 al 7200.

- <span style="color: #236192; font-size: 20px;">fullBurstID</span>
    - Se utiliza para productos [de ráfagas Sentinel-1](/datasets/using_ASF_data/#sentinel-1-bursts). Cada valor representa todos los productos de ráfagas sobre una sola franja, correspondiente a una pila alineada perfectamente con el marco. Este valor es útil para la pila de líneas base. puede especificar un solo valor o una lista de valores.
    - Ejemplo:
        - valor único: fullBurstID='017_034465_IW2'
        - lista de valores: fullBurstID=['017_034465_IW2', '079_167884_IW1']

- <span style="color: #236192; font-size: 20px;">groupID</span>
    - Lista de identificadores de grupo específicos. Para algunos conjuntos de datos, el identificador de grupo es el mismo que el nombre de la escena. Para otros, como Sentinel-1, el identificador de grupo es único para un grupo de escenas.
    - Ejemplo:
        - groupID='S1A_IWDV_0112_0118_037147_150'

- <span style="color: #236192; font-size: 20px;">lookDirection</span>
    - Dirección izquierda o derecha de la adquisición de datos. puede especificar un solo valor.
    - Ejemplo:
        - lookDirection='L'
    - Valores:
        - R, DERECHA, L, IZQUIERDA

- <span style="color: #236192; font-size: 20px;">offNadirAngle</span>
    - Ángulos fuera del nadir para ALOS PALSAR. puede especificar un solo valor, un rango de valores o una lista de valores.
    - Ejemplo:
        - valor único: offNadirAngle=21.5
        - rango de valores: offNadirAngle=(9.7, 14)
        - lista de valores: offNadirAngle=[21.5, 23.1]
    - Valores comunes:
        - Más comunes: 21.5, 23.1, 27.1, 34.3
        - Otros: 9.7, 9.9, 13.8, 14, 16.2, 17.3, 17.9, 18, 19.2, 20.5, 21.5, 23.1, 24.2, 24.6, 25.2, 25.8, 25.9, 26.2, 27.1, 28.8, 30.8, 34.3, 36.9, 38.8, 41.5, 43.4, 45.2, 46.6, 47.8, 49, 50, 50.8

- <span style="color: #236192; font-size: 20px;">polarization</span>
    - Consulta la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/POLARIZATION.py)
    - Una propiedad de las ondas electromagnéticas SAR que se puede utilizar para extraer información significativa sobre las propiedades de la superficie de la Tierra. puede especificar un solo valor o una lista de valores.
    - También puede obtener la lista de constantes disponibles utilizando ```help(asf_search.constants.POLARIZATION)```
    - Ejemplo:
        - polarization=asf.POLARIZATION.VV

- <span style="color: #236192; font-size: 20px;">processingLevel</span>
    - Consulta la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/PRODUCT_TYPE.py)
    - Nivel al que se ha procesado los datos, también es el tipo de producto.
    - También puede obtener la lista de constantes disponibles utilizando ```help(asf_search.constants.PRODUCT_TYPE)```
    - Ejemplo:
        - processingLevel=asf.PRODUCT_TYPE.SLC

- <span style="color: #236192; font-size: 20px;">relativeBurstID</span>
    - Se utiliza para productos [de ráfagas Sentinel-1](/datasets/using_ASF_data/#sentinel-1-bursts). Cada valor identifica un ciclo de ráfagas y dentro de cada subfranja estos valores son únicos. puede especificar un solo valor o una lista de valores.
    - Ejemplo:
        - valor único: relativeBurstID='367299'
        - lista de valores: relativeBurstID=['167877', '167882']

- <span style="color: #236192; font-size: 20px;">relativeOrbit</span>
    - Trayectoria o órbita del satélite durante la adquisición de datos. Para UAVSAR es el [ID de línea](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.201268782.1252483948.1620685771-1930115146.1605056035). puede especificar un solo valor, un rango de valores o una lista de valores.
    - Ejemplo:
        - valor único: relativeOrbit=5905
        - rango de valores: relativeOrbit=(2400, 2410)
        - lista de valores: relativeOrbit=[500, 580]
    - Valores:
        - ALOS: 1-671
        - ERS-1: 0-2410
        - ERS-2: 0-500
        - JERS-1: 0-658
        - RADARSAT-1: 0-342
        - SEASAT: 1-243
        - UAVSAR: varios

### Parámetros Geoespaciales

- <span style="color: #236192; font-size: 20px;">intersectsWith</span>
    - Búsqueda por polígono, segmento de línea ("linestring") o punto definido en el formato Well-Known Text (WKT) en 2D. Cada polígono debe estar explícitamente cerrado, es decir, el primer vértice y el último vértice de cada polígono deben ser idénticos. Las coordenadas para cada vértice están en grados decimales: la longitud sigue a la latitud.
    - Ejemplo:
        - intersectsWith='POLYGON((-152.81 58.49,-154.90 57.49,-155.08 56.30,-153.82 56.34,-151.99 57.30,-151.43 58.19,-152.81 58.49))'
        - intersectsWith='LINESTRING(-119.543 37.925, -118.443 37.7421)'
        - intersectsWith='POINT(-119.543 37.925)'

#### Validación de Forma
Si la AOI especificada es su propio Rectángulo de Contención Mínimo (MBR) en una proyección de Mercator, los resultados de la búsqueda se intersectarán con la AOI en una proyección de Mercator, independientemente de su ancho. Esto sigue siendo cierto incluso si se cruza la línea internacional de cambio de fecha dentro de la AOI.

Para que una AOI sea considerada su propio MBR, debe cumplir con los siguientes criterios:

  - Cada vértice comparte una latitud o longitud con sus vecinos.
  - Los puntos Este/Oeste comparten la longitud.
  - Los puntos Norte/Sur comparten la latitud.

Las AOIs que no cumplen con estos criterios tendrán sus puntos conectados a lo largo de [círculos máximos](https://es.wikipedia.org/wiki/C%C3%ADrculo_m%C3%A1ximo).

Además, todas las AOIs son validadas y, si es necesario, simplificadas según el siguiente proceso:

  1. Validar la AOI de entrada. Si no es válida, se muestra un error.
  2. Fusionar formas que se superpongan.
  3. Cálculo del casco convexo.
  4. Manejo de valores de índice fuera de rango mediante ajuste y envolvimiento a los valores válidos.
  5. Simplificación de puntos según un umbral de proximidad. El objetivo es tener menos de 400 puntos.

Cada uno de estos pasos se realiza solo cuando es necesario para obtener una AOI con un único contorno con menos de 400 puntos. Se omiten los pasos innecesarios.

**Ejemplos de validación y simplificación:**

- Se proporciona un polígono que se auto-intersecta:
    - Se muestra un error.
- Se proporciona un único contorno que consta de 1000 puntos:
    - Se utiliza una versión simplificada del mismo contorno con menos de 400 puntos.
- Se proporcionan múltiples geometrías, todas ellas se superponen al menos en parte:
    - Se devuelve un único contorno que representa el contorno de todas las formas combinadas.
- Se proporcionan múltiples geometrías, al menos algunas de ellas no se superponen en absoluto:
    - Se devuelve un único contorno que representa el casco convexo de todas las formas juntas.

### Parámetros Temporales
- <span style="color: #236192; font-size: 20px;">processingDate</span>
    - Limita los resultados a registros que han sido procesados en ASF desde una fecha y/o hora dada.
    - Ejemplo:
        - processingDate='2017-01-01T00:00:00UTC'

- <span style="color: #236192; font-size: 20px;">start</span>
    - Fecha de adquisición de datos. Puede usarse en combinación con 'end'. puede ingresar fechas en lenguaje natural o un sello de fecha y/o tiempo. Todos los horarios están en UTC.
    - Ejemplo:
        - start='30 de mayo de 2019'
        - start='ayer'
        - start='2010-10-30T11:59:59Z'
        - start='hace 1 semana', end='ahora'

- <span style="color: #236192; font-size: 20px;">end</span>
    - Fecha de adquisición de datos. Puede usarse en combinación con 'start'. puede ingresar fechas en lenguaje natural o un sello de fecha y/o tiempo. Todos los horarios están en UTC.
        - end='30 de mayo de 2018'
        - end='hoy'
        - end='2021-04-30T11:59:59Z'
        - start='hace 1 semana', end='ahora'

- <span style="color: #236192; font-size: 20px;">season</span>
    - Día de inicio y fin del año para el rango estacional deseado. Esta palabra clave puede usarse junto con start/end para especificar un rango estacional dentro de un rango de fechas general. Los valores se basan en el calendario juliano.  especificar tanto una fecha de inicio como una de fin de temporada.
    - Ejemplo:
        - season=[1, 31]
        - season=[45, 67]
        - season=[360, 10]
    - Valores:
        - Del 1 al 365

### Parámetros de Línea de Base
- <span style="color: #236192; font-size: 20px;">stack_from_id</span>
    - Ingrese el nombre de la escena para la cual deseas ver resultados de la línea de base.
    - stack_from_id no puede utilizarse en conjunción con otras palabras clave.
    - Ejemplo:
        - stack_from_id('S1A_IW_SLC__1SDV_20220215T225119_20220215T225146_041930_04FE2E_9252-SLC')
    - Consulta el [cuaderno Jupyter](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/4-Baseline_Search.ipynb) para ejemplos de uso y mejores prácticas.

### Parámetros de Resultados
- <span style="color: #236192; font-size: 20px;">maxResults</span>
    - Número máximo de registros de datos a devolver.
    - Ejemplo:
        - maxResults=10
