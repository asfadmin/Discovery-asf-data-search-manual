# Consejos y Trucos para la API de Búsqueda

¡Esta es una colección de algunos consejos y trucos para la API de Búsqueda!

## Nuevo módulo de Python para realizar búsquedas
`asf_search` es un módulo de Python para realizar búsquedas en el catálogo de ASF. Además, ofrece funcionalidad básica y soporte de descarga. Está disponible a través de PyPi y Conda. Puedes encontrar más información [aquí](/asf_search/basics).

## Limitación de velocidad en el punto final de búsqueda
Se ha implementado una limitación de velocidad en el [punto final de búsqueda](/api/keywords/#search-endpoint). La limitación de velocidad es por dirección IP y actualmente es de 250 consultas por minuto. Al alcanzar el límite, las consultas adicionales devolverán un HTTP 429 con un mensaje de error. Verifica si tus consultas están devolviendo un pequeño número de resultados. Si es así, puedes refinar tus parámetros para combinar conjuntos de resultados en grupos más grandes y luego procesar esos resultados localmente. Por ejemplo, en lugar de buscar en una pequeña área de interés con una consulta individual para cada día, selecciona un rango de fechas más amplio para crear una sola consulta, luego divide los resultados después de haberlos recuperado.

## Copiar/Pegar URL de la API de Búsqueda desde Vertex
¿Has completado una búsqueda geoespacial en Vertex que te gustaría replicar en una consulta de la API de Búsqueda? Haz clic en la flecha hacia abajo debajo de "Max Results". Elige "API URL...".

Aquí puedes ver la URL de la API de Búsqueda que utilizarías para replicar la búsqueda. Puedes cambiar el número máximo de resultados y el formato de salida. Una vez que estés satisfecho, haz clic en el icono de copia. Ahora puedes pegar la consulta en un navegador o interfaz de línea de comandos para ejecutarla.

## Encontrar el Valor de Product_List en Vertex
El nombre del producto/archivo se encuentra en los Resultados de Búsqueda de Vertex, en la columna de detalles de los archivos. Puedes hacer clic en el icono de copia para copiar el ID del archivo. También puedes copiar todos los ID de archivos desde tu cola de descargas en Vertex. Una vez que tengas la lista deseada de archivos, puedes encontrarlos a través de la API de Búsqueda utilizando la palabra clave "product_list".

## Los Resultados de Búsqueda Pueden Convertirse en un Área de Búsqueda
Puedes convertir tus resultados de búsqueda en un área de búsqueda. Primero, exporta tus resultados de búsqueda en formato de salida GeoJSON o KML. Luego, importa tu archivo en la búsqueda geoespacial de Vertex. Vertex extraerá el Área de Interés (AOI) de tu archivo. Si lo deseas, puedes agregar filtros y guardar tus filtros de búsqueda o la búsqueda misma.

## Verificar que tu Consulta Devuelva el Número Correcto de Resultados
¿Te gustaría verificar que tu consulta haya devuelto el número correcto de resultados? Cambia tu salida a "output=count" para verificarlo. Si el recuento no coincide, considera acotar tu búsqueda utilizando más palabras clave o utilizando la palabra clave "maxResults" para limitarla. También puedes intentar acortar el rango de fechas para dividir tu búsqueda en una serie de búsquedas más pequeñas.
