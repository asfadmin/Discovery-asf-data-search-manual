# Descarga

## Autenticación de sesión

asf_search admite la descarga de datos, tanto de los resultados de búsqueda proporcionados por las funciones de búsqueda, como directamente en las URL de los productos. Por lo general, se requiere una sesión autenticada. asf_search utiliza '''Solicitudes''. El uso de credenciales .netrc es el método preferido para la autenticación. Puede encontrar más información sobre la autenticación .netrc [aquí](https://requests.readthedocs.io/en/latest/user/authentication/#netrc-authentication).

Ejemplo usando .netrc:

	resultados = ....
	results.download(path='....')

Si no utiliza credenciales .netrc, puede autenticarse mediante un objeto ''ASFSession''' y uno de los siguientes métodos de autenticación. '''ASFSession''' es una subclase de '''Session''. La sesión debe pasarse a cualquier método de descarga al que se llame, se puede reutilizar y es seguro para subprocesos. 

- '''auth_with_creds('usuario', 'pasar)'''
- '''auth_with_token('EDL token')'''
- '''auth_with_cookiejar(http.cookiejar)'''

Ejemplo con autenticación manual:

	resultados = asf_search.granule_search([...])
	sesión = asf_search. ASFSession().auth_with_creds('usuario', 'pass')
	results.download(path='/Users/SARGuru/data', session=session)

asf_search también admite la descarga de una lista arbitraria de URL. Se admiten todos los métodos de autenticación disponibles:

	urls = [...]
	asf_search.download_urls(urls=urls, path='/Users/SARGuru/data', session=ASFSession().auth_with_token('EDL token'))

Tenga en cuenta también que ''ASFSearchResults.download()''' y la función genérica '''download_urls()''' aceptan un parámetro ''procesos''' que permite descargas paralelas.

## Métodos
### <span style="color: #236192; tamaño de fuente: 20px;" >download_urls()</span>

Descarga todos los productos de las direcciones URL especificadas a la ubicación especificada.

**args**

- urls: Lista de URLs desde las que descargar
- path: ruta local en la que guardar el producto
- sesión: La sesión a utilizar, en la mayoría de los casos debe ser autenticada de antemano
- procesos: Número de procesos de descarga a utilizar. El valor predeterminado es 1 (es decir, descarga secuencial)

### <span style="color: #236192; tamaño de fuente: 20px;" >download_url()</span>

Descarga un producto desde la dirección URL especificada a la ubicación especificada y al nombre de archivo (opcional).

**args**

- url: URL desde la que descargar
- path: ruta local en la que guardar el producto
- filename: Nombre de archivo opcional a utilizar, extraído de la URL por defecto
- sesión: La sesión a utilizar, en la mayoría de los casos debe ser autenticada de antemano

### <span style="color: #236192; tamaño de fuente: 20px;" >remotezip()</span>

Configura y devuelve un ''remotezip autenticado. Objeto RemoteZip'', que permite descargar
Archivos específicos de un archivo zip determinado sin descargar todo el archivo.

**args**

- url: URL desde la que descargar un archivo zip
- sesión: ''ASFSession''' autenticado que RemoteZip usará para descargar desde el producto zip

**Devuelve:**

- 'RemoteZip. Objeto RemoteZip' autenticado con el objeto _ASFSession_ pasado

## Formatos de exportación
asf_search proporciona varios formatos de exportación, además del formato de asf_search predeterminado. Los formatos disponibles son: geojson, csv, metalink, kml, jsonlite, jsonlite2.

Ejemplos:

	resultados = ....
	con open("search_results.csv", "w") como f:
		f.writelines(resultados.csv())

	resultados = ....
	con open("search_results_jsonlite.json", "w") como f:
		f.writelines(results.jsonlite())

