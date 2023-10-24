#ResultadosdelabúsquedadeASF
## Descripción

Esta clase describe un conjunto de resultados de búsqueda del archivo ASF. La clase proporciona una forma conveniente de administrar y examinar los resultados de búsqueda, así como la funcionalidad de exportación y descarga.

***

## Atributos
- 'searchOptions' _(ASFSearchOptions)_: Las opciones de búsqueda utilizadas para generar este conjunto de resultados. Puede ser 'Ninguno' en algunos casos.
- 'searchComplete' _(bool)_: Bandera que significa 'asf_search.search()' completada con éxito recopilando resultados de CMR. 
***

## Métodos

### <span style="color: #236192; tamaño de fuente: 20px;" >download()</span>

Itera sobre cada ''ASFProduct''' y los descarga en la ruta especificada.

**args:**

- ruta: El directorio en el que se deben descargar los productos.
- sesión: La sesión a utilizar, en la mayoría de los casos debe ser autenticada de antemano.
- procesos: Número de procesos de descarga a utilizar. El valor predeterminado es 1 (es decir, descarga secuencial)
- fileType _(opcional)_: Se utiliza para descargar metadatos XML de Burst. Especifique '''fileType=asf. FileDownloadType.ADDITIONAL_FILES'''' para descargar los metadatos XML. Para descargar archivos .tiff y .xml para ráfagas, use '''asf. FileDownloadType.ALL_FILES''''
	- Ejemplo: ''''burst_results.download(session=session, path="./", fileType=asf. FileDownloadType.ADDITIONAL_FILES)''''
	- Nota: Los metadatos XML de ráfaga son un archivo generado virtualmente y, por lo tanto, no tienen su propio nombre de archivo único. Los metadatos XML solo se pueden encontrar a través del nombre de la escena de ráfaga.

**devoluciones:** Ninguna

***

### <span style="color: #236192; tamaño de fuente: 20px;" >geojson()</span>

'ASFSearchResults.__str__()' utiliza este método para la serialización a través de 'json.dumps()'

**args:** Ninguno

**Devuelve:**

- 'dict' que describe los resultados de la búsqueda como un objeto geojson.

### <span style="color: #236192; tamaño de fuente: 20px;" >csv()</span>

Crea un generador de cadenas con formato csv a partir de los resultados

**args:** Ninguno

**Devuelve:**

- Un generador de cadenas con formato csv

### <span style="color: #236192; tamaño de fuente: 20px;" >kml()</span>

Crea un generador de cadenas con formato KML a partir de los resultados

**args:** Ninguno

**Devuelve:**

- Un generador de cadenas con formato kml

### <span style="color: #236192; tamaño de fuente: 20px;" >metalink()</span>

Crea un generador de cadenas con formato de metavínculo a partir de los resultados

**args:** Ninguno

**Devuelve:**

- Un generador de cadenas con formato de metavínculo

### <span style="color: #236192; tamaño de fuente: 20px;" >raise_if_incomplete()</span>

Utilícelo para comprobar si los resultados devueltos por 'asf_search.search()' están incompletos (esto puede suceder
si se produce un error al consultar CMR)

**args:** Ninguno

**Plantea:**

- Genera un 'asf_search.exceptions.ASFSearchError' si los resultados están incompletos
