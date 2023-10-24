# Opciones de búsqueda de ASF

## Descripción

Esta clase describe un conjunto de parámetros de búsqueda. Si bien no es necesario utilizar esta clase al construir una búsqueda, puede ser útil, ya que proporciona cierto grado de validación inmediata de parámetros, así como una forma conveniente de manipular y manejar las opciones de búsqueda en general.

Los parámetros de búsqueda específicos se manejan como atributos de objeto. Al intentar agregar un atributo que no es compatible, se generará un KeyError. Si intenta eliminar un atributo, se establecerá en Ninguno. Los parámetros de búsqueda se pueden establecer a través de kwargs en la instancia del objeto, o directamente en un objeto existente utilizando los mecanismos normales.

La conversión a un "dictado" solo incluirá opciones de búsqueda que realmente se hayan establecido en un valor utilizable. Es decir, se ignorarán todas las opciones establecidas en 'Ninguna'.



## Atributos
- maxResults
- absoluteBurstID
- absoluteOrbit
- asfFrame
- beamMode
-proveedor
- collectionName
- maxDoppler
- minDoppler
- maxFaradayRotación
- minFaradayRotation
- flightDirection
- flightLine
- fullBurstID
-marco
- granule_list
- product_list
- intersectaCon
- lookDirection
- offNadirAngle
-plataforma
-polarización
- processingLevel
- relativeBurstID
- relativeOrbit
- fecha de procesamiento
-empezar
-fin
-estación
- groupID
- insarStackId
-instrumento
-sesión



## Métodos

_ASFSearchOptions no proporciona ningún método destinado al uso directo, sino que depende de un puñado de dunders para el comportamiento deseado. Para mayor claridad, estos se incluyen below._

### <span style="color: #236192; tamaño de fuente: 20px;" >__init__()</span>

Establece los diversos atributos descritos anteriormente y procesa cualquier kwargs en ellos.

**args:**

- _**kwargs_, limitado a los nombres enumerados como atributos anteriores. Cualquier otra cosa generará un 'KeyError'

**Devuelve:**
Ninguno



### <span style="color: #236192; tamaño de fuente: 20px;" >__setattr__()</span>

Establece el atributo denominado por 'clave' en el 'valor' especificado después de pasarlo a través de una función de validación adecuada.

Los valores de 'Ninguno' están permitidos como una forma de anular el atributo. Al intentar establecer una 'clave' que no aparece en la lista de atributos anterior, se generará un 'KeyError'

**args:**

- key: el nombre del atributo a establecer
- valor: el valor en el que se debe establecer el atributo nombrado

**Devuelve:**
Ninguno



### <span style="color: #236192; tamaño de fuente: 20px;" >__delattr__()</span>

Borra los nombres de un atributo por 'elemento' configurándolo en 'Ninguno'

**args:**

- item: el nombre del atributo que se va a borrar

**Devuelve:**
Ninguno



### <span style="color: #236192; tamaño de fuente: 20px;" >__iter__()</span>

Se utiliza al convertir el objeto ASFSearchOptions en objetos más fundamentales, como 'dict'

Solo incluye atributos que no son 'Ninguno'.

**args:**
Ninguno

**Rendimientos:**

- (clave, valor) pares para cada uno de los atributos anteriores que no son 'Ninguno'



