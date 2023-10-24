# Conceptos básicos de la API de búsqueda

La creación de una consulta de la API de búsqueda consta de 3 pasos básicos:

1. Utilice la URL base de la API de búsqueda: https://api.daac.asf.alaska.edu
2. Elija un punto final. Todos los puntos finales disponibles se enumeran en la [Documentación de palabras clave](/api/keywords). El extremo de búsqueda usa esta dirección URL base: https://api.daac.asf.alaska.edu/services/search/param
3. Cree su consulta usando [palabras clave](/api/palabras clave)

La URL completada estará en este formato: https://api.daac.asf.alaska.edu/services/search/param?keyword1=value1&keyword2=value2,value3&keyword3=value4-6

Una vez que se genera la consulta, puede ejecutarla copiando/pegando en una ventana del explorador, una interfaz de línea de comandos o mediante un programa. Puede encontrar más detalles sobre varias opciones y algunas sugerencias de sintaxis en la [documentación de Search API Tools](/api/tools).

- no encuentro los links



**Descarga de datos**

Para descargar datos, necesitará una cuenta de inicio de sesión de NASA EOSDIS Earthdata. Las cuentas de Earthdata son gratuitas. Vaya a [Earthdata Login — Create Profile](https://urs.earthdata.nasa.gov/users/new) para crear una cuenta.

Se le pedirá que acepte el Acuerdo de licencia de usuario final de ASF y establezca un Área de estudio para completar su nueva configuración de usuario.

*Nota: Se requiere un acuerdo de investigación para acceder a los datos de JERS-1 y RADARSAT-1. Complete el [Acuerdo de investigación] requerido (https://asf.alaska.edu/restricted-data-access-request) o comuníquese con el servicio de atención al usuario en el correo electrónico o número a continuación.*

**Próximos pasos**

Consulte [Buscar palabras clave de API](/api/keywords) para empezar a crear una consulta, o consulte la [Página de herramientas](/api/tools) para ver algunos ejemplos.

Alternativamente, es posible que desee utilizar asf_search, un módulo de Python para realizar búsquedas en el catálogo de ASF. También ofrece funcionalidad básica y soporte de descarga. Además, se proporcionan numerosas constantes para facilitar el proceso de búsqueda. Está disponible a través de PyPi y Conda. Puede encontrar más información [aquí](/asf_search/basics).