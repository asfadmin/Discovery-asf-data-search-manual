# Conceptos básicos de búsqueda_asf

## Visión general

asf_search es un módulo de Python para realizar búsquedas en el catálogo ASF. Además, ofrece funcionalidad básica y soporte de descarga. Está disponible a través de PyPi y Conda.

	importación asf_search como ASF

	Resultados = asf.granule_search(['ALPSRS279162400', 'ALPSRS279162200'])
	imprimir(resultados)

	wkt = 'POLÍGONO((-135,7 58,2,-136,6 58,1,-135,8 56,9,-134,6 56,1,-134,9 58,0,-135,7 58,2))'
	Resultados = asf.geo_search(platform=[asf. PLATAFORMA. SENTINEL1], intersectsWith=wkt, maxResults=10)
	imprimir(resultados)

Para obtener un tutorial introductorio de asf_search, consulte [Jupyter Notebooks](https://github.com/asfadmin/Discovery-asf_search/tree/master/examples).

## Instalación
Para administrar fácilmente las dependencias, recomendamos utilizar entornos de proyecto dedicados a través de [Anaconda / Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) o [entornos virtuales Python](https://docs.python.org/3/tutorial/venv.html).

asf_search se puede instalar en un entorno conda con

	conda install -c conda-forge asf_search

o en un entorno virtual con

	python -m pip instalar asf_search

## Uso
La búsqueda mediante programación de datos de ASF se simplifica con asf_search. Se proporcionan varias funciones de búsqueda. Cada función de búsqueda devuelve un objeto ```ASFSearchResults```:

- ```geo_search()``` Buscar información del producto en un área de interés usando una cadena WKT
- ```granule_search()``` Buscar información del producto usando una lista de nombres de escenas
- ```product_search()``` Buscar información del producto utilizando una lista de ID de producto
- ```stack_from_id()``` Buscar una pila de línea base de productos utilizando una escena de referencia
- Si los enfoques de búsqueda anteriores no satisfacen sus necesidades de búsqueda, ```search()``` admite todas las palabras clave disponibles:
	- ```search()``` Buscar información del producto utilizando cualquier combinación de parámetros de búsqueda
- Además, se proporcionan numerosas constantes para facilitar el proceso de búsqueda. Actualmente, proporcionamos constantes para el modo de haz, la dirección de vuelo, el instrumento, la plataforma, la polarización y el tipo de producto. Puedes ver la [lista completa de constantes aquí](https://github.com/asfadmin/Discovery-asf_search/tree/master/asf_search/constants).

Además, asf_search admite la descarga de datos, tanto de los resultados de búsqueda proporcionados por las funciones de búsqueda anteriores, como directamente en las URL de los productos. Por lo general, se requiere una sesión autenticada. Puede encontrar más información sobre los métodos de autenticación disponibles [aquí](https://requests.readthedocs.io/en/latest/user/authentication/). También puede autenticarse mediante un objeto ```ASFSession``` y uno de los siguientes métodos de autenticación. ASFSession es una subclase de "Session".

- ```auth_with_creds('usuario', 'pasar)```
- ```auth_with_token('EDL token')```
- ```auth_with_cookiejar(http.cookiejar)```

Si no se utilizan credenciales .netrc, esa sesión debe pasarse al método de descarga al que se llame, se puede reutilizar y es seguro para subprocesos.

Ejemplo usando .netrc:

	resultados = ....
	results.download(path='....')

Ejemplo con autenticación manual:

	Resultados = asf_search.granule_search([...])
	sesión = asf_search. ASFSession().auth_with_creds('usuario', 'pass')
	results.download(path='/Users/SARGuru/data', session=session)

Alternativamente, asf_search admite la descarga de una lista arbitraria de URL. Se admiten todos los métodos de autenticación disponibles:

	urls = [...]
	asf_search.download_urls(urls=urls, path='/Users/SARGuru/data', session=ASFSession().auth_with_token('EDL token'))

Tenga en cuenta también que ```ASFSearchResults.download()``` y la función genérica ```download_urls()``` aceptan un parámetro ```procesos``` que permite descargas paralelas.

Se pueden encontrar más ejemplos de todo lo anterior en este [script de ejemplo](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/hello_world.py)



