# Novedades

## Nuevo módulo de Python para realizar búsquedas
`asf_search` es un módulo de Python para realizar búsquedas en el catálogo de ASF. Además, ofrece funcionalidad básica y soporte de descarga. Está disponible a través de PyPi y Conda. Puedes encontrar más información [aquí](/asf_search/basics).

## Múltiples puntos finales disponibles

Además del punto final de búsqueda, tenemos varios puntos finales disponibles para todas tus necesidades de API de búsqueda. A continuación, se presenta una breve descripción de lo que está disponible. Puedes encontrar más detalles sobre estos puntos finales y cómo utilizarlos en la [página de Palabras clave](/api/keywords).

**Punto final de línea base**

Este punto final se puede utilizar para buscar datos de referencia específicos.

**Puntos finales WKT**

El punto final de validación WKT validará y reparará una entrada WKT. El punto final de archivos geoespaciales a WKT aceptará una solicitud POST con archivos adjuntos. Devolverá el WKT analizado del archivo, así como el WKT reparado con y sin envolver.

**Punto final del analizador de fechas**

Este punto final se puede utilizar para verificar cómo se analizan las fechas mediante la API de búsqueda.

**Punto final de lista de misiones**

Este punto final enumera todas las misiones (también conocidas como campañas o colecciones) de todos los conjuntos de datos.

**Punto final de estado de salud**

Este punto final se utiliza para verificar el estado de salud de la API de búsqueda. También proporciona información sobre el estado de salud de CMR.

## Formato de salida preferido de la API de búsqueda

El formato GeoJSON es el formato de salida preferido de la API de búsqueda. Puedes especificar el formato de salida con la palabra clave "output". Si encuentras un campo requerido que no está incluido en la salida GeoJSON, por favor, contacta a ASF utilizando la información a continuación o comunícate directamente con el equipo en <uaf-asf-discovery@alaska.edu>.
