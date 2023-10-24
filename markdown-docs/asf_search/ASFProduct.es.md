# ASFProductos

## Descripción

Esta clase describe un único producto del archivo ASF. La clase proporciona metadatos, así como varios métodos útiles para interactuar con el producto.



## Atributos
- 'properties' _(dict)_: Proporciona metadatos del producto como el modo de haz, la hora de inicio, etc.
- 'geometría' _(dict)_: Describe las extensiones físicas del producto como un fragmento geojson.
- 'baseline' _dict_: Los campos relacionados con la línea base del producto, si están disponibles en CMR.
- 'mmm' _(dict)_: la respuesta json de mmm sin procesar de CMR utilizada para rellenar 'propiedades', 'geometría', 'línea base' y 'meta'.
- 'meta' _(dict)_: los metadatos json devueltos de CMR.
<!-- netrc
Cómo construir un archivo Netrc, enlace
O auth con estas opciones en su lugar -->



## Métodos

### <span style="color: #236192; tamaño de fuente: 20px;" >geojson()</span>

'ASFProduct.__str__()' utiliza este método para la serialización a través de 'json.dumps()'

**args:**
Ninguno

**Devuelve:**

- 'dict' que describe el producto como un fragmento de geojson.



### <span style="color: #236192; tamaño de fuente: 20px;" >download(ruta, _filename=Ninguno, sesión=None_)</span>

Descarga este producto en la ruta de acceso especificada y en el nombre de archivo opcional.

**args:**

- ruta: El directorio en el que se debe descargar este producto.
- filename _(opcional)_: Nombre de archivo a utilizar en lugar del nombre de archivo original de este producto.
- sesión _(opcional)_: La sesión a utilizar, en la mayoría de los casos debe ser autenticada de antemano. Si no se proporciona ninguna sesión, se utilizará una sesión en blanco (no autenticada).
- fileType _(opcional)_: Se utiliza para descargar metadatos XML de Burst. Especifique '''fileType=asf. FileDownloadType.ADDITIONAL_FILES'''' para descargar los metadatos XML. Para descargar archivos .tiff y .xml para ráfagas, use '''asf. FileDownloadType.ALL_FILES''''
	- Ejemplo: ''''burst_results.download(session=session, path="./", fileType=asf. FileDownloadType.ADDITIONAL_FILES)''''
	- Nota: Los metadatos XML de ráfaga son un archivo generado virtualmente y, por lo tanto, no tienen su propio nombre de archivo único. Los metadatos XML solo se pueden encontrar a través del nombre de la escena de ráfaga.

**Devuelve:**
Ninguno



### <span style="color: #236192; tamaño de fuente: 20px;" >stack()</span>

Crea una pila de línea base utilizando este producto como referencia

**args:**

- cmr_provider _(opcional)_: Nombre de proveedor personalizado para restringir los resultados de CMR a, para obtener más información sobre cómo se usa, consulte [documentación de CMR](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#c-provider)
- session _(opcional)_: Una sesión que se utilizará al realizar la búsqueda. Para la mayoría de los usos, se puede ignorar. Se utiliza cuando se busca un conjunto de datos, proveedor, etc. que requiere autenticación. Consulte [ASFSession](/asf_search/ASFSession) para obtener más detalles.
- host _(opcional)_: host de SearchAPI, por defecto a Production SearchAPI. Esta opción está pensada para fines de desarrollo y pruebas y, por lo general, se puede omitir.

**Devuelve:**

- ''ASFSearchResults''' representación de la pila, con la adición de valores de línea base (temporal, perpendicular) adjuntos a cada 'ASFProduct'



### <span style="color: #236192; tamaño de fuente: 20px;" >get_stack_opts()</span>

Crea opciones de búsqueda que describen una pila InSAR basada en este producto. Similar a 'stack()' pero no realiza la búsqueda, simplemente devuelve ''ASFSearchOptions''' que puede ser inspeccionado o ajustado y luego pasado a varias funciones de búsqueda.

**args:**
Ninguno

**Devuelve:**

- Objeto '''ASFSearchOptions'''



### <span style="color: #236192; tamaño de fuente: 20px;" >centroide()</span>

Determina el centroide de un producto.

**args:**
Ninguno

**Devuelve:**

- '''shapely.geometry.point.Point''' objeto que describe el centroide del producto

<!-- Tendrá más que exportación geojson; Agregue esto cuando otras opciones de salida disponibles -->

### <span style="color: #236192; tamaño de fuente: 20px;" >remotezip()</span>

Devuelve un objeto RemoteZip configurado, que permite descargar partes seleccionadas del archivo zip de un producto.
Para obtener más información sobre cómo usar remotezip con asf-search, consulte la sección 'Descarga de productos individuales' de [el bloc de notas jupyter de ejemplo](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/5-Download.ipynb). Para obtener más información sobre el paquete remotezip de código abierto, consulte <a target="_blank" href="https://github.com/gtsystem/python-remotezip">the remotezip project repo</a>.

**args:**

- 'session' _ASFSession_: Un objeto _ASFSession_ autenticado que se utilizará para descargar el producto

**Devuelve:**

- '''remotezip. Objeto RemoteZip''' autenticado con el objeto _ASFSession_ pasado
