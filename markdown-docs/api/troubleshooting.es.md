# Solución de problemas de la API de búsqueda

Si está solucionando problemas de consultas de API de búsqueda, considere la posibilidad de usar asf_search. asf_search es un módulo de Python para realizar búsquedas en el catálogo ASF. Puede encontrar más información [aquí](/asf_search/basics).

**Área de problemas: la consulta devuelve HTTP 429 con mensaje de error**

- Motivo: La consulta devuelve HTTP 429 con el mensaje de error "Tasa limitada, reduzca la tasa de solicitud a 250 / minuto o menos"
- Remedio: Existe una limitación de velocidad en el punto final de búsqueda. Consulte [Limitaciones de tasa](/api/cookbook/#rate-limitation-on-search-endpoint) para obtener consejos sobre cómo crear sus consultas. 

**Área de problemas: "protocolo no reconocido" de cURL de Windows**

- Motivo: comillas dobles invisibles insertadas al copiar/pegar ejemplos
- Remedio: Eliminar las comillas visibles, lo que eliminará las comillas invisibles. A continuación, vuelva a escribir las comillas.

**Área problemática: La descarga falla con "401 no autorizado" o "Error de autorización"**

- Motivo: Falta o no es válido el nombre de usuario/contraseña de Earthdata
- Remedio: Compruebe que está incluyendo correctamente su nombre de usuario y contraseña de Earthdata en su comando de descarga o archivo de configuración.

**Área problemática: La descarga falla con "401 no autorizado" o "Error de autorización"**

- Motivo: Caracteres especiales en la contraseña de Earthdata
- Remedio: Las contraseñas con caracteres especiales deberán estar entre comillas.

**Área problemática: No se puede autenticar**

- Motivo: Falta el área de estudio o EULA
- Remedio: Inicie sesión en Earthdata y asegúrese de que su área de estudio esté configurada, y que haya aceptado todos los acuerdos de licencia de usuario final necesarios.

**Área problemática: falla la solicitud de API de búsqueda con '+' **

- Motivo: Algunos valores de palabras clave pueden contener espacios.
- Remedio: Intente reemplazar el '+' por '%2B'. Para obtener más detalles, consulte Codificación de caracteres en la [Página de herramientas](/api/tools).

**Área problemática: error en la solicitud de la API de búsqueda**

- Motivo: se requiere https
- Remedio: Asegúrese de que está utilizando https, no http.

**Área problemática: la solicitud de la API de búsqueda se bloquea, falla o devuelve un error**

- Motivo: Su URL puede incluir espacios o caracteres especiales.
- Remedio: Consulte Codificación de caracteres en la [página Herramientas](/api/tools) y asegúrese de que está codificando espacios y caracteres especiales correctamente.

**Área problemática: la API de búsqueda devuelve un error de validación**

- Motivo: El motivo del error de validación se incluye en el mensaje de error devuelto.
- Remedio: Refine sus palabras clave y valores según sea necesario. Si no está seguro de por qué recibió el error de validación, puede comunicarse con ASF utilizando la información a continuación.

**Área problemática: la consulta de la API de búsqueda no devuelve el número esperado de resultados**

- Motivo: Hay un límite de tiempo de 15 minutos para ejecutar consultas de la API de búsqueda.
- Remedio: Primero, intente la misma consulta con "output = count". Si el recuento es alto, considere limitar su búsqueda usando más palabras clave o usando la palabra clave "maxResults" para limitarlo. También puede intentar acortar el rango de fechas para dividir su búsqueda en una serie de búsquedas más pequeñas.

**Área problemática: la consulta de la API de búsqueda con la palabra clave "product_list" no devuelve resultados**

- Motivo: Otras palabras clave pueden estar compitiendo con el valor product_list valor(es).
- Remedio: Intente eliminar otras palabras clave de su consulta. También puede probar "output=count" para ver cuántos resultados debe devolver su consulta.

**Área problemática: el formato de salida seleccionado no incluye los campos necesarios**

- Motivo: Algunos formatos de salida incluyen diferentes campos.
- Remedio: GeoJSON es el formato predeterminado preferido. Si no se incluye un campo obligatorio, comuníquese con ASF utilizando la información a continuación o comuníquese con el equipo directamente a <uaf-asf-discovery@alaska.edu>

<!-- - Área problemática: Certificado rechazado
	- Motivo: Certificados de terceros desactualizados, un problema para las búsquedas https
	- Remedio: Utilice http O deshabilite las comprobaciones de certificados.
		- [rizo](https://curl.se/docs/manpage.html) –inseguro
		- [wget](https://www.gnu.org/software/wget/) –no-check-certificate
 -->
