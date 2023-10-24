# Palabras clave de la API de búsqueda

Considera el uso de nuestro nuevo módulo de Python, asf_search. asf_search se puede utilizar para realizar búsquedas en el catálogo de ASF y ofrece funcionalidad básica y soporte para descargas. Además, se proporcionan numerosas constantes para facilitar el proceso de búsqueda. Actualmente, proporcionamos constantes para plataforma, instrumento, modo de haz, dirección de vuelo, polarización y nivel de procesamiento. Puedes encontrar más información [aquí](/asf_search/basics).

Las palabras clave se utilizan para encontrar los datos deseados. Usa tantas o tan pocas palabras clave como necesites. Las palabras clave disponibles y sus descripciones se enumeran a continuación para cada punto final de la API de búsqueda. Las palabras clave son sensibles a mayúsculas y minúsculas.

*Nota:* Cualquier error se devolverá en formato JSON.

## Punto de acceso de búsqueda
<https://api.daac.asf.alaska.edu/services/search/param>

### Parámetros del conjunto de datos
- <span style="color: #236192; font-size: 20px;">plataforma</span>
    - Esta palabra clave tiene constantes proporcionadas a través de asf_search. Puedes encontrar más información [aquí](/asf_search/searching/#keywords).
    - Ver también 'instrumento'
    - Plataforma de percepción remota que adquirió los datos. Sentinel-1 y ERS tienen múltiples plataformas de percepción remota, y puedes elegir si deseas especificar una plataforma específica. Puedes especificar un solo valor o una lista de valores.
    - Ejemplo:
        - plataforma=ALOS
        - plataforma=SA,SB
        - plataforma=S1
    - Valores:
        - ALOS, A3, AIRSAR, AS, ERS, ERS-1, E1, ERS-2, E2, JERS-1, J1, RADARSAT-1, R1, SEASAT, SS, S1, Sentinel, Sentinel-1, Sentinel-1A, SA, Sentinel-1B, Sentinel-1 Interferogram (BETA), SB, SIR-C, SMAP, SP, UAVSAR, UA

- <span style="color: #236192; font-size: 20px;">instrumento</span>
    - Esta palabra clave tiene constantes proporcionadas a través de asf_search. Puedes encontrar más información [aquí](/asf_search/searching/#keywords).
    - Ver también 'plataforma'
    - Instrumento de percepción remota que adquirió los datos. Para algunas plataformas, como ALOS, hay varios instrumentos para elegir.
    - Ejemplo:
        - ALOS: instrumento=PALSAR
        - ALOS: instrumento=AVNIR-2
    - Valores:
        - C-SAR, PALSAR, AVNIR-2

- <span style="color: #236192; font-size: 20px; font-size: 20px;">órbitaAbsoluta</span>
    - Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
    - Para ALOS, ERS-1, ERS-2, JERS-1, RADARSAT-1, Sentinel-1A y Sentinel-1B, este valor corresponde al recuento de órbitas dentro del ciclo de órbita. Para UAVSAR, es el [ID de vuelo](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.34282209.1335434931.1620087198-1930115146.1605056035). Puedes especificar un solo valor, un rango de valores o una lista de valores.
    - Ejemplo:
        - RADARSAT: órbitaAbsoluta=25436
        - PALSAR: órbitaAbsoluta=25436-25445,25450
        - UAVSAR: órbitaAbsoluta=12006

- <span style="color: #236192; font-size: 20px;">asfframe</span>
    - Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
    - Ver también 'frame'
    - Esto es principalmente una referencia de marco de ASF / [JAXA](https://global.jaxa.jp/). Sin embargo, algunas plataformas utilizan otras convenciones. Puedes especificar un solo valor, un rango de valores o una lista de valores.
    - Ejemplo:
        - asfframe=300 o asfframe=2845-2855 o asfframe=2800,2845-2855
    - Valores:
        - ERS, JERS, RADARSAT: Marcos ASF de 0 a 900
        - ALOS PALSAR: Marcos JAXA de 0 a 7200
        - SEASAT: Marcos similares a la ESA de 0208 a 3458 (debe usar un cero principal para los marcos 208-999)
        - Sentinel-1: Valores internos de 0 a 1184

- <span style="color: #236192; font-size: 20px;">maxBaselinePerp</span>
    - Para análisis SAR interferométrico (InSAR), la Línea de Base Perpendicular es la distancia espacial entre las primeras y segundas observaciones medida perpendicular a la dirección de observación del satélite y proporciona una indicación de la sensibilidad a la altura topográfica.
    - Funciona para ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (No para Sentinel-1)
    - Ejemplo:
        - maxBaselinePerp=1500 o maxBaselinePerp=50.5

- <span style="color: #236192; font-size: 20px;">minBaselinePerp</span>
    - Para análisis SAR interferométrico (InSAR), la Línea de Base Perpendicular es la distancia espacial entre las primeras y segundas observaciones medida perpendicular a la dirección de observación del satélite y proporciona una indicación de la sensibilidad a la altura topográfica.
    - Funciona para ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (No para Sentinel-1)
    - Ejemplo:
        - minBaselinePerp=100 o minBaselinePerp=50.5
