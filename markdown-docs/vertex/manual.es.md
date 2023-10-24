#Guía de Inicio de Vertex

- Si aún no tiene  una **[cuenta Earthdata](https://urs.earthdata.nasa.gov/users/new)** puede crear una gratis.
- Vaya a **[Vertex](https://search.asf.alaska.edu)**
	- Inicie sesión haciendo clic en el ícono de **Iniciar sesión** en la esquina superior derecha de la ventana. Utiliza su nombre de usuario y contraseña de Earthdata.
![type:video](https://www.youtube.com/embed/j_Db_ipKLos)
- El tipo de búsqueda le permite elegir entre todos los tipos de búsqueda disponibles.

##Opciones de Idioma

En el menú en la esquina superior derecha, junto al ícono de **Iniciar sesión**, hay opciones de control de idioma. Vertex actualmente ofrece inglés y español. Si su navegador está configurado en uno de los idiomas disponibles, Vertex se ajustará automáticamente a ese idioma. Puede hacer clic en el botón y seleccionar su idioma deseado en la lista desplegable. También puede establecer un idioma predeterminado en tus **Preferencias**.

##Opciones de Búsqueda *Geográfica*

![type:video](https://www.youtube.com/embed/JovQ-rG9ZJE)

- En la esquina superior izquierda del mapa, hay botones que le permiten cambiar su **proyección de mapa**, **zoom** y **vista de mapa**.
	- Por defecto, el mapa está en proyección ecuatorial. Puede hacer clic en **Ver de mapa** y seleccionar **Ver de mapa ártico** o **Ver de mapa antártico** para cambiar la proyección del mapa. Haz clic en **Ver  de mapa ecuatorial** para volver a la proyección ecuatorial.
	- Puede hacer clic en los íconos de **Acercar** o **Alejar** para ajustar el zoom.
	- La capa de mapa por defecto es satélite. puede hacer clic en el botón **Capas** y seleccionar **Vista de satélite** o **Vista de calle** para cambiar la capa de mapa.
		- Puede hacer clic en **Mapa de resumen** para agregar un mapa de resumen en la esquina superior derecha del mapa. Haz clic nuevamente para desactivar el mapa de resumen.
		- Puede hacer clic en **Líneas de cuadrícula** para agregar una superposición de graticule al mapa. Haz clic nuevamente para desactivar la superposición. *Nota*: Esto actualmente solo está disponible en la vista de mapa ecuatorial.
	- Puede hacer clic en **Opacidad** y ajustar el deslizador según desee para cambiar la opacidad de las imágenes de navegación que se muestran en el mapa.
- Navega hasta su área de interés arrastrando el mapa mientras mantienes presionado el botón izquierdo del mouse.
- Por defecto, la herramienta de dibujo en el mapa es un cuadro delimitador. Haz clic en el mapa una vez para especificar la esquina inicial, mueve el mouse y luego haga clic nuevamente para terminar el cuadro. Hay opciones adicionales de herramientas de dibujo disponibles en la barra de herramientas en la parte superior de la pantalla, que incluyen opciones de *punto*, *línea* y *polígono*.
	- **Punto** le permite definir un área de interés haciendo clic en el mapa para colocar un punto.
	- **Línea** le permite definir un área de interés sobre una serie de segmentos de línea haciendo clic en el mapa varias veces. Haz doble clic para detener la adición de segmentos.
	- **Polígono** le permite definir un área de interés sobre un polígono arbitrario. Recibirás un mensaje de error en la parte inferior de la ventana si hubo algún problema con el polígono (autointersección, orden inverso del polígono, etc.).
	- **Cuadro** le permite definir un área de interés sobre un cuadro delimitador alineado con latitud/longitud haciendo clic una vez para establecer una esquina y nuevamente para establecer la esquina opuesta.
	- Una vez que se haya dibujado una forma, selecciona el ícono de **Editar área de interés actual** en la barra de herramientas para mover, agregar y eliminar puntos. Selecciona el ícono de **Dibujar nueva área de interés** para crear una nueva AOI.
	- Hacer clic en **Cargar archivo geoespacial** abre la ventana de diálogo de Área de interés. Puede ingresar una cadena WKT, cargar un archivo geoespacial o ingresar una ubicación.
- **Conjunto de datos** le permite elegir el conjunto de datos de interés.
	- Si necesita más información sobre un conjunto de datos en particular, haga clic en el ícono de interrogación correspondiente en el selector de Conjunto de datos.
- **Filtros...** le permite refinar aún más su búsqueda

### Opciones de Área de Interés

- **Área de Interés** le brinda la opción de ingresar un conjunto de coordenadas geográficas, importar un área de interés como un archivo geoespacial o buscar una ubicación. Haga clic en la flecha hacia abajo junto a **Área de Interés** en el menú superior.
	- Un área de interés se puede definir mediante un conjunto de coordenadas ingresadas en la ventana **Área de Interés WKT**.
		- Las coordenadas deben ingresarse en grados decimales en formato *texto bien conocido* (WKT). Las coordenadas ingresadas como una cadena de longitud/latitud separadas por comas (por ejemplo, -97.38,36.46,-53.44,36.46...) se convertirán automáticamente a formato WKT por Vertex.
	- Para cargar un archivo geoespacial, haga clic en **Seleccionar archivos** y navegue hasta una carpeta en su computadora o arrastra y suelta archivos en el cuadro. Se admiten archivos *GeoJSON*, *shapefiles* y *KML* siempre que estén en un sistema de coordenadas basado en latitud/longitud, como WGS84.
		- Al importar un archivo *GeoJSON*, se incluirán todas las geometrías en el archivo. Si se encuentran múltiples geometrías, se utilizará una envolvente convexa para representarlas en la búsqueda.
		- Los *shapefiles* pueden ser un solo archivo *.shp*, múltiples componentes de archivo shapefile (*.shp, .shx, .dbf*), o un archivo *zip* que contenga uno o más componentes de archivo shapefile. En todos los casos, se debe incluir como mínimo el componente *.shp*.
	- Para ingresar una ubicación, haga clic en el campo **Buscar una ubicación** y comienza a escribir el nombre de la ubicación. Selecciona la ubicación deseada en la lista desplegable.
		- Una vez que hayas seleccionado una ubicación, se convertirá en coordenadas en formato WKT.
	- Puede guardar las coordenadas de una búsqueda para poder recrear exactamente un área de interés en búsquedas posteriores.
		- Una vez que se haya configurado el **Área de Interés**, aparecerá un ícono de *Copiar al portapapeles*. Haga clic en el ícono y pegue las coordenadas en una nueva búsqueda o en un archivo de texto para usarlas más tarde.
		- Nota: Consulta la sección **Otras Opciones de Vertex** para conocer formas adicionales de guardar búsquedas.
	- En cualquier momento, puede borrar su área de búsqueda haciendo clic en el botón **Borrar**.

#### Validación de Forma
Si el AOI especificado es su propio Rectángulo Mínimo Delimitador (MBR) en una proyección mercator, los resultados de la búsqueda devueltos se intersectarán con el AOI en una proyección mercator, independientemente del ancho. Esto sigue siendo válido incluso si la línea de cambio de fecha internacional se cruza dentro del AOI.

Para que un AOI se considere su propio MBR, debe cumplir con los siguientes criterios:

  - Cada vértice comparte una latitud o longitud con sus vecinos
  - Los puntos Este/Oeste comparten longitud
  - Los puntos Norte/Sur comparten latitud

AOIs que no cumplan con estos criterios tendrán sus puntos conectados a lo largo de [círculos máximos](https://es.wikipedia.org/wiki/C%C3%ADrculo_m%C3%A1ximo).

Además, todos los AOIs se validan y se simplifican según sea necesario. El proceso para ello es:

  1. Validar el AOI de entrada. Si no es válido, se mostrará un error.
  2. Fusionar formas superpuestas.
  3. Envoltura convexa.
  4. Cualquier valor de índice fuera de rango se maneja mediante la restricción y el ajuste a la gama de valores válidos.
  5. Simplificar puntos según el umbral de proximidad. El objetivo es tener menos de 400 puntos.

Cada uno de estos pasos se realiza solo cuando es necesario para obtener el AOI con un solo contorno con menos de 400 puntos. Cualquier paso innecesario se omite.

**Ejemplos de validación y simplificación:**

  - Se proporciona un polígono que se interseca a sí mismo:
    - Se muestra un error.
- Se proporciona un esquema único, compuesto por 1000 puntos:
     - Se utiliza una versión simplificada del mismo esquema, compuesta por menos de 400 puntos.
- Se proporcionan múltiples geometrías, superponiéndose todas ellas al menos en parte:
	- Se devuelve un único contorno, que representa el contorno de todas las formas combinadas.
- Se proporcionan múltiples geometrías, al menos algunas de ellas no se superponen en absoluto:
	   -Se devuelve un contorno único, que representa el casco convexo de todas las formas juntas.

### Filtros de fecha

- **Filtros de fechas** Las fechas de búsqueda son opcionales, por lo que están vacías de forma predeterminada. Si está buscando fechas específicas, puede definir más el rango de fechas en los campos **Fecha de inicio** y **Fecha de final**. El selector de fechas limitará automáticamente su selección a un rango válido para el conjunto de datos seleccionado.
	- *Nota*: esta información también se puede encontrar haciendo clic en el icono del signo de interrogación de un conjunto de datos.
 	- **Búsqueda estacional** permite restringir la búsqueda a ciertos períodos anuales dentro de un rango general de fechas. Haga clic en el botón de búsqueda de temporada y aparecerán opciones adicionales que le permitirán ingresar un rango de fechas general (*Fecha de inicio/Fecha de final*) y el rango estacional (*Día de inicio de temporada/Día de finalización de temporada*).

### Filtros adicionales

![type:video](https://www.youtube.com/embed/Vd9eDL9KVK4)

- **Filtros adicionales** permiten aplicar parámetros adicionales para acotar la búsqueda y reducir el número de resultados. No todos los filtros estarán disponibles para todos los conjuntos de datos.
	- **Tipo de archivo** – Limita la búsqueda a tipos específicos de archivos. Se permiten varias selecciones.
	- **Modo de haz** – Limita la búsqueda a modos de haz específicos. Se permiten varias selecciones.
	- **Polarización** – Limita la búsqueda a polarizaciones específicas. Se permiten varias selecciones.
	- **Dirección** – Limita la búsqueda a una dirección de órbita específica.
	- **Subtipo** – Limita la búsqueda a una nave espacial de misión específica.

### Filtros de ruta y marco

- **Los filtros de ruta y fotograma** están disponibles para determinados conjuntos de datos. Puede introducir un solo trazado o fotograma, o un intervalo. Debido a la inconsistencia del encuadre de Sentinel-1, recomendamos buscar un fotograma de interés por ±1-2 fotogramas.
- El número máximo de resultados se muestra debajo del botón **BUSCAR**. Haga clic en la **flecha hacia abajo** para elegir los resultados máximos que prefiera.
	- Puede hacer clic en **URL de API...** para generar la URL de la API que coincida con sus parámetros de búsqueda actuales. Esto abrirá una nueva ventana.
		- **Cantidad** le permite establecer los resultados máximos.
		- **Formato** le permite elegir el formato de salida que prefieras.
		- El icono **Copiar** junto a la URL copiará la URL. Se puede pegar en la barra de búsqueda de un navegador para realizar la API buscar, o pegar en un documento y guardar.
		- **API Docs** te enviará a la [API Documentación](https://asf.alaska.edu/api/).
		- **Descargar resultados** descargará los resultados en el formato de salida especificado.
- Una vez que se hayan elegido todos los parámetros, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán en el área de pie de página de la ventana Vértice y en el mapa.
	- *Nota*: El número de archivos que se prevé que coincidan con los parámetros de búsqueda actuales se muestra debajo del botón BUSCAR. Si no hay coincidencias previstas, el botón de búsqueda aparecerá atenuado y mostrará SIN RESULTADOS.

## *Lista* Opciones de búsqueda

![type:video](https://www.youtube.com/embed/oetqxZkqVZM)

- Al seleccionar **Búsqueda en lista** se abre la ventana *Búsqueda en lista* y le permite ingresar una lista de escenas o nombres de archivo.
	- **Escena** permite buscar nombres de escenas específicas (nombres de gránulos), y los resultados incluirán cualquier archivo que forme parte de esas escenas.
	- **Archivo** permite buscar nombres de archivo específicos (nombres de productos), y los resultados solo incluirán exactamente esos archivos.
- **Editar lista** abre la ventana *Búsqueda de lista* para que pueda realizar cambios en tu lista
- Una vez que se hayan elegido todos los parámetros, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán en el área de pie de página de la ventana de tu navegador y en el mapa.
	- *Nota*: El número de archivos que se prevé que coincidan con los parámetros de búsqueda actuales se muestra debajo del botón BUSCAR. Si no hay coincidencias previstas, el botón de búsqueda aparecerá atenuado y mostrará SIN RESULTADOS.

### Importación de archivos de búsqueda de listas
Puede **arrastrar y soltar archivos** en el cuadro provisto en las pestañas **Escena** o **Archivo**. Cada pestaña enumera los tipos de archivos aceptados en la parte inferior. Vertex analizará los nombres de escena o archivo de tu archivo cargado.

- *Nota*: Cada tipo de archivo requiere un formato específico. Los archivos exportados desde Vertex tendrán el formato correcto.

- **CSV** requiere una columna etiquetada como "Nombre del gránulo" para una búsqueda en la lista de escenas. Requiere una columna adicional "Nivel de procesamiento" para una búsqueda en la lista de archivos.
- **GeoJSON** requiere un campo etiquetado como "granuleName" para la búsqueda en la lista de escenas. Requiere un campo etiquetado como "fileID" para la búsqueda en la lista de archivos.
- **Metalink** requiere una estructura formateada como
```
<metalink>
    <archivos>
        <nombre de archivo="[Nombre-escena.zip]"></archivo>
        <nombre del archivo ="...
        ... </archivo>
    </archivos>
</metalink>
```

- **KML** requiere una estructura formateada como
```
<kml>
    <Documento>
        <Marca de posición>
            <nombre>[Nombre de la escena]</nombre>
        </Marca de posición>
    </Documento>
</kml>
```

## *Línea de base* Opciones de búsqueda

![type:video](https://www.youtube.com/embed/Xp5bgvi2pEM)

- Al seleccionar **Búsqueda de línea base** se proporciona un espacio para introducir el nombre de una escena de referencia y, a continuación, se buscarán todas las escenas secundarias que coincidan con el área de cobertura de la referencia.
	- *Nota*: Si no hay escenas coincidentes, el botón RESULTADOS aparecerá atenuado y mostrará SIN RESULTADOS.
- Una vez que se haya ingresado una escena de referencia, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán debajo del mapa. Al hacer clic en el icono *Acercar a los resultados* en la parte superior de la columna de resultados de la izquierda, se mostrará la ubicación de la pila de escenas en el mapa.
- El gráfico muestra la relación temporal y perpendicular (espacial) de las escenas secundarias con la referencia.
- Al hacer clic en **Criterios de línea de base...** encima del gráfico, se abrirá la ventana de *Búsqueda de línea de base*. Con los controles deslizantes, las extensiones temporal y perpendicular se pueden ajustar para limitar el número de escenas secundarias que se muestran en los resultados.
- Para obtener más información sobre **Línea de base**, consulte la [Documentación de línea de base](/vertex/baseline).

## *SBAS* Opciones de búsqueda

![type:video](https://www.youtube.com/embed/bQPdtuobdcg)

- Al seleccionar **Búsqueda SBAS** se proporciona un espacio para introducir el nombre de una escena de referencia y se buscarán todas las escenas secundarias que coincidan con el área de cobertura de la referencia. Es un método alternativo utilizado para el procesamiento de SAR interferométrico (InSAR), similar a la línea de base.
	- *Nota*: Si no hay escenas coincidentes, el botón RESULTADOS aparecerá atenuado y mostrará SIN RESULTADOS.
- Una vez que se haya ingresado una escena de referencia, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán debajo del mapa. Al hacer clic en el icono *Acercar a los resultados* en la parte superior de la columna de resultados de la izquierda, se mostrará la ubicación de la pila de escenas en el mapa.
- El gráfico muestra la relación temporal y perpendicular (espacial) de las escenas secundarias con la referencia.
	- Los botones **Acercar** y **Alejar** están disponibles encima del gráfico.
	- El botón **Zoom to Fit** garantiza que todos los pares sean visibles en el gráfico.
	- Los botones **Emparejamiento personalizado** le permiten agregar o eliminar un par personalizado.
	- El botón **Criterios SBAS...** le permite especificar criterios adicionales para refinar los resultados, como las fechas de inicio y finalización, la configuración de fechas estacionales y la configuración del umbral de superposición latitudinal.
- Para obtener más información sobre **SBAS**, consulte la [documentación de SBAS](/vertex/sbas).

## *Evento* Opciones de búsqueda

- Seleccionar **Evento** le permite ver y buscar los productos creados para el monitoreo de peligros.
- **Búsqueda de eventos** le permite introducir un nombre de evento. Puede introducir el nombre completo o una cadena parcial.
- **Tipos de eventos** le permite filtrar los tipos de eventos que deseas ver. Actualmente, hay eventos sísmicos y volcánicos.
- **Fecha de inicio** y **Fecha de finalización** le permiten especificar un intervalo de fechas para los eventos.
- Se pueden encontrar opciones adicionales en **Filtros**.
	- Puede activar el interruptor **Solo eventos activos** para mostrar solo los eventos activos. El valor predeterminado es mostrar todos los eventos, incluidos los eventos inactivos.
	- Puede ajustar el control deslizante **Magnitud** para filtrar los terremotos por el rango de magnitud deseado. *Nota:* Este filtro solo se aplica a eventos sísmicos. Si tu búsqueda incluye volcanes, estos seguirán apareciendo en los resultados de búsqueda.
- Para obtener más información sobre la búsqueda de **Eventos**, consulte la [Documentación de búsqueda de eventos](/vertex/events).

## *Productos On Demand* Opciones de búsqueda

- La selección de **Productos On Demand** le permite ver los trabajos On Demand enviados. *Nota*: Debes iniciar sesión para acceder a esto. Si no ha iniciado sesión, esta opción de búsqueda aparecerá atenuada y no podrá seleccionarla.
- **Nombre del proyecto** le permite limitar tu búsqueda a un nombre de proyecto específico. A medida que comiences a escribir, las opciones de autocompletar estarán disponibles con los nombres de proyecto que hayas utilizado anteriormente.
- **Filtros de fecha** Las fechas de búsqueda son opcionales, por lo que de forma predeterminada están vacías.  Si está buscando fechas específicas, puede definir el rango de fechas con más detalle en los campos **Fecha de inicio** y **Fecha de finalización**. *Nota*: Estas fechas filtran por la fecha de la escena, no por la fecha en que se procesó.
- **Escena de producto/origen** le permite introducir el nombre del producto o el nombre de la escena de origen para limitar tu búsqueda. Este campo también aceptará una cadena parcial de la escena del producto o de la escena de origen en lugar del nombre completo.
- **Estado del trabajo** le permite limitar tu búsqueda a estados específicos. Se permiten varias selecciones.
- *Nota*: Los trabajos caducan 14 días después de enviarlos. Los productos caducados siguen apareciendo en los resultados de búsqueda, sin embargo, ya no puede descargarlos ni añadirlos a tu carrito. Puede identificar fácilmente tus productos caducados por la etiqueta **Caducado** junto al nombre del producto.
- Para obtener más información sobre **Productos On Demand**, consulte la [documentación](https://hyp3-docs.asf.alaska.edu/).

## *Conjuntos de datos derivados* Opciones de búsqueda

- La selección de **Conjuntos de datos derivados** le permite ver y descargar productos del catálogo de conjuntos de datos de ASF.
- Cada conjunto de datos enumerado incluye una breve descripción.
- Haga clic en **Más información** para ver más información sobre el conjunto de datos.
- Haga clic en **Descargar** para ver y descargar los productos disponibles para el conjunto de datos elegido. *Nota*: El enlace de descarga se abrirá en una nueva ventana del navegador.
- Para obtener más información sobre **Conjuntos de datos derivados**, consulte la [Documentación de conjuntos de datos derivados](/vertex/derived_datasets/).

## Resultados de la búsqueda

![type:video](https://www.youtube.com/embed/wp8Xt_Y4T84)

- En Vertex, se considera que una **escena** es un paquete que contiene todos los **archivos**, o productos, que están relacionados con una ubicación y hora específicas.
	- *Por ejemplo*, la columna de la izquierda del panel Resultados muestra las escenas devueltas de una búsqueda. La columna de la derecha muestra el contenido del archivo de cada escena.
- El número máximo de archivos que devolverá una búsqueda se muestra en el botón BUSCAR.
	- Este número se puede ajustar haciendo clic en la flecha hacia abajo.
	- También se muestra el número total de archivos que coinciden con los parámetros de búsqueda.
- La barra de encabezado de Resultados.
	- El botón **Zoom** se acercará a la ubicación de todas las escenas en el mapa.
	- El botón **Lista** añadirá todas las escenas a la lista de descarga.
	- El botón **On Demand** te permitirá elegir qué escenas elegibles agregar a la lista On Demand para tu posterior procesamiento.
	- El botón **Raw** mostrará u ocultará los archivos RAW. *Nota*: Este botón solo se aplica a las escenas de Sentinel-1.
	- El botón **Exportar** te permitirá exportar datos o metadatos de todas las escenas de los resultados.
	- El botón **Caducado** mostrará u ocultará los archivos On Demand caducados. *Nota*: Este botón solo está disponible en el tipo de búsqueda **Productos On Demand**.
	- *Nota*: No todos los botones están disponibles en todos los tipos de búsqueda.
- La columna **Escenas** (izquierda).
	- Haga clic en el icono del carrito junto al nombre de una escena para agregar todos los archivos de la escena a la lista de descarga. El carrito cambia de apariencia cuando se hace esto.
	- Haga clic en el icono de zoom junto al nombre de una escena para acercarse a la ubicación de la escena en el mapa.
- Para ver más información sobre una escena, haga clic en la escena en la columna de la izquierda y se completarán las columnas **Detalle de escena** y **Archivos**.
	- La columna **Detalle de la escena** (centro) proporciona una descripción más detallada de la escena, incluyendo *Fecha/Hora de inicio*, *Modo de haz*, *Trayectoria*, *Fotograma*, *Dirección de vuelo*, *Polarización*, *Órbita absoluta* y una imagen de exploración (si está disponible). No todas las escenas tendrán toda la información adicional.
		- El botón **Herramienta de línea base** abre la herramienta Línea base ASF, que se utiliza para crear Pilas InSAR.
		- El botón **Herramienta SBAS** abre la herramienta ASF SBAS, que es otro método para crear Pilas InSAR.
		- El botón **Más como esto** crea una búsqueda basada en la ruta y el fotograma de la escena seleccionada.
		![type:video](https://www.youtube.com/embed/h7vmrcpMd60)
		- El botón **Citar** abre una nueva ventana con una guía de citas para trabajos publicados que utilizan datos, imágenes o herramientas a las que se accede a través de ASF.
		- **Descargar esta imagen** descarga la imagen de navegación.
		- El icono del ojo con la etiqueta **Abrir en el visor de imágenes** abre una ventana de visualización de exploración más grande.
			- En el visor de exploración, **zoom** con los botones **+** o **-**. También puede hacer zoom y desplazarse con el ratón.
			- Haga clic o desplácese por las miniaturas de la parte inferior para ver otras imágenes de exploración de las escenas devueltas por la búsqueda.
			- De forma predeterminada, la casilla **Mostrar solo escenas con una imagen de exploración** está marcada. Puede desmarcar esta opción para ver todas las escenas devueltas por tu búsqueda. Las escenas sin una imagen de exploración mostrarán una lista en miniatura *No hay exploración disponible*.
			- Los metadatos de la escena se muestran en el lado derecho de la ventana del visor de exploración.
	- La columna **Archivos** (derecha) muestra una lista de archivos disponibles para la escena seleccionada actualmente. Puede descargar archivos inmediatamente o agregarlos a tu lista de descarga haciendo clic en el icono correspondiente.
		- Al hacer clic en la flecha derecha frente al nombre de un archivo (producto), se expandirá el archivo para mostrar los archivos auxiliares incluidos. Estos archivos pueden descargarse individualmente o añadirse a la lista de descarga.
			- Debes estar firmado en Vertex para que esta función funcione.
			- Esta función no está disponible para todos los conjuntos de datos.

## On Demand

![type:video](https://www.youtube.com/embed/AxhYMBzycuY)

- Al hacer clic en el icono de **tres casillas** en el encabezado, etiquetado como **On Demand**, se mostrará una lista desplegable de opciones.
- **On Demand Queue** abrirá la lista On Demand.
	- Los diferentes Los tipos de trabajos de la lista están separados por pestañas en la parte superior de la lista. Los tipos de trabajo disponibles actualmente son **RTC GAMMA**, **InSAR GAMMA** y **autoRIFT**. Puede hacer clic en una pestaña para seleccionarla. La pestaña seleccionada está resaltada.
	- Para **RTC GAMMA** y **En los trabajos de GAMMA** de SAR, hay opciones de procesamiento adicionales disponibles.  Las opciones que seleccione se aplicarán a todos los archivos de ese tipo de trabajo en la lista.
		- Puede pasar el cursor sobre cada opción para mostrar una información sobre herramientas con detalles sobre la opción.
	- Elija la clasificación deseada con los cuadros desplegables **Criterios de clasificación** y **Orden de clasificación**.
		- En **Criterios de ordenación**, puede optar por ordenar los archivos por *Fecha de inicio* del archivo o por *Fecha de adición* a la lista.
		- En **Orden de clasificación**, puede optar por ordenar los archivos por *Más reciente* o más reciente, o por *Más antiguo*.
	- La lista de archivos que ha agregado a tu lista se muestra debajo de las opciones. La X le permite eliminar cualquier archivo que desee de la lista.
	- **Borrar** mostrará una lista de algunas opciones para borrar archivos de la lista. Puede optar por borrar una pestaña individual o puede elegir **Borrar todos los tipos de procesamiento** para borrar todos los archivos de la lista. Si elige borrar todos los archivos, se mostrará la opción *Restaurar* para permitirle deshacer esta acción.
	- El número de trabajos restantes se muestra en la parte inferior de la lista. Hay 1.000 trabajos asignados a cada usuario al mes. Si tiene demasiados trabajos en la lista, se mostrará un mensaje que indica el número de trabajos adicionales en la parte superior de la lista. El**El botón Sumbit** aparecerá atenuado.
	- Cuando esté satisfecho con sus selecciones, haga clic en **Enviar trabajos** en la parte inferior. Esto mostrará la ventana Envío de revisión.
		- El campo **Nombre del proyecto** le permite crear un nombre para los archivos que desea enviar para tu procesamiento. El límite de caracteres es de 20. Este campo es opcional.
		- Puede seleccionar o anular la selección de las casillas de verificación para enviar solo los tipos de trabajo que desee.
		- Seleccione **Cancelar** para volver a la lista sin enviar ningún archivo para tu procesamiento.
		- Haga clic en **Enviar** para enviar sus trabajos. *Nota:* El botón Enviar mostrará el número de trabajos que está enviando.
		- Si hay algún error, como la falta de cobertura DEM, se mostrará un mensaje de error.
- **Productos enviados** cambiará al tipo de búsqueda Productos On Demand y mostrará los productos enviados.
- **On Demand (HyP3) Docs** te enviará a la [Documentación On Demand](https://hyp3-docs.asf.alaska.edu/)
- *Nota*: Debes iniciar sesión para ver tus productos enviados y enviar trabajos desde la On Demand.

## Lista de descargas

![type:video](https://www.youtube.com/embed/cRjqbLNv4Aw)

La funcionalidad mejorada de la lista de descarga ya está disponible en el navegador Google Chrome. Consulte [a continuación](/vertex/manual/#google-chrome-browser) para obtener más información.

- Al hacer clic en el **icono del carrito** en el encabezado, etiquetado como **Descargas**, se mostrará el contenido de tu lista de descarga actual.
	- Dentro de la lista de descarga, se muestra la lista de archivos que ha seleccionado para descargar con información básica sobre cada archivo, como el tipo y el tamaño del archivo.
		- Los ID de archivo (nombres) se pueden copiar con el icono **copiar**.
		- Los archivos se pueden descargar individualmente con el icono de **nube**. También puede hacer clic con el botón derecho para guardar o copiar la URL de descarga.
		- Los elementos se pueden eliminar de la lista con la **X**.
	- **Borrar** borrará todos los archivos de la lista. Se mostrará la opción *Restaurar* para permitirle deshacer esta acción.
	- **Copiar ID de archivo** copiará los nombres de archivo de todos los archivos de la lista para usarlos en otro lugar. Por ejemplo, esta lista podría pegarse en la ventana *Búsqueda de lista*.
	- **Copiar URLs** copiará las URLs de descarga de todos los archivos de la lista.
	- **Descarga de datos** se utiliza para descargar varios productos, ya sea con el *Script de descarga de Python (.py)* o *Metalink (metalink)* opción de archivo.
	- **Descarga de metadatos** se utiliza para exportar el contenido de la lista de descarga a un archivo *CSV*, *KML* o *GeoJSON*. Los archivos *KML* y *GeoJSON* proporcionados por esta característica son compatibles con la función *Importación de búsqueda geográfica*.

### Navegador Google Chrome

La funcionalidad mejorada de la lista de descarga está disponible en el navegador Google Chrome. Tenga en cuenta que esta funcionalidad mejorada no es compatible con el modo incógnito.

- Haz clic en el **icono del carrito** en el encabezado, con la etiqueta **Descargas** para abrir la lista de descargas.
	- Al lado de cada archivo, puede hacer clic en el icono de la **nube** para comenzar la descarga.
		- A medida que comienza la descarga, un indicador de progreso enumera el porcentaje descargado. Una vez que el La descarga se ha completado, el icono aparece como una **marca de verificación** para indicar que el archivo se ha descargado.
		- Mientras se descarga el archivo, puede hacer clic en el indicador de progreso para detener la descarga.
	- En **Descarga de datos**, puede seleccionar **Descargar todo**. Esto descargará 3 archivos a la vez hasta que se hayan descargado todos los productos de tu carrito. Se mostrarán los mismos indicadores de progreso y marcas de verificación para informarle sobre el estado de cada descarga en tu lista.
		- Al hacer clic en **Descargar todo**, aparecerá un cuadro de diálogo:
			1. Navegue a la carpeta donde desea guardar los archivos y haga clic en *Seleccionar*.
			2. Haga clic en *Ver archivos* para permitir que la descarga continúe.
			3. Haga clic en *Guardar cambios* para guardar las preferencias de la carpeta de descarga. Esto persistirá mientras la ventana del navegador de vértices permanezca abierta.
	- Si **borra** los productos de la lista, se restablecerán los indicadores de progreso y finalización de la descarga. Puede volver a añadir los productos a tu lista si lo desea.
	- *Nota*: Debes iniciar sesión para descargar archivos. Si no ha iniciado sesión, cuando haga clic para iniciar una descarga, se le redirigirá primero a la página de inicio de sesión.

## Otras opciones del Vertex

- En la esquina superior izquierda del mapa, hay botones que te permiten cambiar tu **proyección de mapa**, **zoom** y **ver de mapa**. *Nota:* Los controles de mapa disponibles varían según el tipo de búsqueda.
![type:video](https://www.youtube.com/embed/qrUnsbZTVnA)
	- De forma predeterminada, el mapa está en proyección ecuatorial. Puede hacer clic en **Ver mapa** y seleccionar **Ver mapa del Ártico** o **Ver mapa de la Antártida** para cambiar la proyección del mapa. Haga clic en **Ver mapa ecuatorial** para volver a la proyección ecuatorial.
	- Puede hacer clic en los iconos **Acercar** o **Alejar** para ajustar tu zoom.
	- La capa de mapa predeterminada es satélite. Puede hacer clic en el botón **Capas** y seleccionar **Vista de satélite** o **Vista de calle** para cambiar la capa del mapa.
		- Puede hacer clic en **Mapa general** para agregar un mapa general en la esquina superior derecha del mapa. Vuelva a hacer clic en él para desactivar el mapa de vista general.
		- Puede hacer clic en **Líneas de cuadrícula** para agregar una superposición de retícula al mapa. Vuelva a hacer clic en él para desactivar la superposición. *Nota*: Actualmente, esto solo está disponible en la vista de mapa ecuatorial.
	- Puede hacer clic en **Opacidad** y ajustar el control deslizante como desee para cambiar la opacidad de las imágenes de navegación que se muestran en el mapa.
- Haga clic en la **flecha hacia abajo** en la **Búsqueda**
	- **Borrar búsqueda** borrará todos los parámetros de búsqueda que se hayan establecido, excepto el tipo de búsqueda y el conjunto de datos.
	- **Búsquedas guardadas** abre un submenú.
	![type:video](https://www.youtube.com/embed/io4OQumWrJA)
		- **Guardar búsqueda** le permite nombrar y guardar tu búsqueda actual.
		- **Ver búsquedas...** abre una lista de búsquedas que ha nombrado y guardado. Haga clic en el icono de la lupa para cargar la configuración de búsqueda.
		- **Historial de búsquedas...** abre una lista de sus 10 últimas búsquedas que no fueron nombradas ni guardadas. Haga clic en el icono de la lupa para cargar la configuración de búsqueda.
	- **Filtros guardados** abre un submenú.
		- **Guardar filtros** le permite guardar tu conjunto de filtros actual.
		- **Ver filtros...** le permite ver sus conjuntos de filtros guardados. Haga clic en Aplicar filtros para aplicarlos a tu búsqueda actual.
	- **Compartir búsqueda** abre un submenú.
		- **Copiar enlace de búsqueda** copiará todos los parámetros de búsqueda que se hayan establecido en la búsqueda actual como una URL. A continuación, la URL se puede pegar en la barra de búsqueda del navegador para volver a crear la búsqueda exactamente, o pegado en un documento y guardado para volver a crear la búsqueda más tarde.
		- **Compartir con correo electrónico** abrirá un nuevo correo electrónico con la URL de la búsqueda para enviarlo a otras personas.
	- **Ayuda y tutoriales** proporciona demostraciones ilustradas y en video sobre los pasos básicos para configurar una búsqueda y ver los resultados.
		- *Nota*: Debes estar firmado en Vertex para que estas opciones estén disponibles.
	- **Exportar** abre un submenú.
		- **Exportar Python** proporcionará un fragmento de código de Python para recrear la búsqueda actual utilizando el módulo de búsqueda de Python asf_search. También proporciona un enlace a la documentación asf_search.
		- **Exportar API** proporcionará la URL de la API para volver a crear la búsqueda actual usando el comando SearchAPI. También proporciona un vínculo a la documentación de SearchAPI.
- Haga clic en **Ayuda** para ver opciones de ayuda adicionales.
	- **Mira nuestros tutoriales** proporciona demostraciones ilustradas y en video sobre cómo usar Vertex.
	- **Lea nuestra Guía del usuario** abre la documentación de Vertex en una nueva pestaña.
	- **Lea nuestro On Demand Guide** abre la documentación de On Demand en una nueva pestaña.
	- **Buscar datos SAR mediante la API de ASF** abre el archivo SearchAPI en una nueva pestaña.
	- **Más información sobre la PPA y el SAR** abre el sitio web de la PPA en una nueva pestaña.
	- **Estadísticas y repositorio de GitHub** proporciona enlaces a nuestro repositorio de GitHub Vertex.
- Haga clic en el icono **Iniciar sesión** una vez que haya iniciado sesión para mostrar las opciones de usuario.
	- **Búsquedas guardadas** abre una lista de búsquedas que ha nombrado y guardado. Haga clic en el icono de la lupa para cargar la configuración de búsqueda.
	- **Historial de búsquedas** abre una lista de sus 10 últimas búsquedas que no fueron nombradas ni guardadas. Haga clic en el icono de la lupa para cargar la configuración de búsqueda.
	- **Filtros guardados** abre una lista de filtros que ha guardado. Haga clic en *Aplicar filtros* para aplicar el conjunto de filtros seleccionado a tu búsqueda.
	- **Preferencias** abre una ventana que le permite establecer las preferencias de búsqueda para el idioma, el tema, el dataset, los resultados máximos, la capa de mapa y los ajustes preestablecidos de filtro predeterminados. Estas preferencias se guardarán y se aplicarán a futuras búsquedas.
- *Nota*: **Búsquedas guardadas**, **Filtros guardados** e **Historial de búsqueda** están disponibles tanto en el menú Iniciar sesión como en el menú de flecha hacia abajo del botón Buscar.
- Haga clic en el campo **Buscar en todos los ASF** en la barra de encabezado gris para realizar una búsqueda. Las entradas en este campo buscarán en todos los sitios web de ASF.
	- También puede hacer clic en el icono de **micrófono** si prefieres utilizar la búsqueda por voz.
	- A medida que escribas o hables, los resultados de tu búsqueda se mostrarán en una lista debajo del campo. Al hacer clic en un resultado de la lista, se abrirá una nueva pestaña del navegador.
	- Puede hacer clic en el icono de **lupa** para expandir los resultados de la búsqueda. Esto se abrirá en la misma ventana del navegador. Para cerrar y volver a Vértice, haz clic en la **X** cerca de la parte superior derecha de la pantalla.
