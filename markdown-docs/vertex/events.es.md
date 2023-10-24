# Tipo de Búsqueda de Eventos

## ¿Qué es la Búsqueda de Eventos?
La búsqueda de eventos aprovecha las capacidades del procesamiento SAR para monitorear desastres naturales. Los peligros actualmente admitidos son erupciones volcánicas y terremotos. Los productos generados incluyen series temporales de imágenes completamente corregidas en cuanto al terreno, así como datos SAR interferométricos sobre áreas afectadas por desastres naturales. Para facilitar la automatización completa, el flujo de procesamiento se desencadena automáticamente mediante sistemas de alerta de peligro existentes, como el Servicio de Notificación de Terremotos del USGS. El monitoreo de eventos a través de Vertex se basa en la tecnología desarrollada dentro de SARVIEWS a través de la subvención NNX12AQ38G. Visita la [documentación de Eventos (SARVIEWS)](/datasets/events_about) para obtener más información.

## Cómo usar la Búsqueda de Eventos de Vertex
Visita **[Vertex de ASF](https://search.asf.alaska.edu)** para comenzar a usar la búsqueda de eventos.

### **Comenzando tu Búsqueda de Eventos**

- Cuando seleccionas el tipo de búsqueda **Evento**, se realizará una búsqueda y se mostrarán todos los eventos disponibles. Al igual que con otros tipos de búsqueda, hay filtros disponibles para limitar o refinar tus resultados de búsqueda.
- Haz clic en **Búsqueda de Evento** para ingresar un nombre de evento o un nombre parcial. También puedes seleccionar el evento deseado en la lista desplegable que se muestra cuando haces clic en el campo.
- Bajo **Tipos de Eventos**, puedes elegir qué tipos de eventos deseas que se muestren. Actualmente, hay eventos de Terremotos y Volcanes.
- Puedes seleccionar una **Fecha de Inicio** o una **Fecha de Finalización**.
- Haz clic en **Filtros** para más opciones.
	- Puedes activar o desactivar el interruptor de **Solo Eventos Activos** para mostrar solo eventos activos. El valor predeterminado es mostrar todos los eventos, incluidos los eventos inactivos.
	- Puedes ajustar el control deslizante de **Magnitud** para filtrar terremotos según el rango de magnitud deseado. *Nota:* Este filtro se aplica solo a eventos de terremotos. Si tu búsqueda incluye volcanes, estos seguirán apareciendo en tus resultados de búsqueda.
- Una vez que hayas seleccionado tus filtros deseados, haz clic en **Buscar** para actualizar tus resultados de búsqueda.

#### **Filtros de Productos**
- Los **Filtros de Ruta y Cuadro** están disponibles. Puedes ingresar una sola ruta o cuadro o un rango.
	- Haz clic en **Limpiar** para borrar los valores de ruta y cuadro ingresados.
	- Ten en cuenta que **Ruta y Cuadro** filtrarán los productos mostrados dentro de cada evento.
- Bajo **Tipo de Producto**, puedes seleccionar uno o más tipos de productos. Esto filtrará los productos mostrados dentro de cada evento.

### **Interacción con los Resultados de la Búsqueda de Eventos**
Mientras estás en el tipo de búsqueda de eventos, notarás muchos controles familiares en el panel de resultados. Los eventos se muestran en la columna izquierda. Los íconos de Volcán y Terremoto indican qué tipo de evento es cada resultado. La columna central enumera los detalles y metadatos del evento seleccionado. Los archivos para el evento seleccionado se muestran en la columna derecha.

**Controles del Panel de Resultados**

- En la parte superior izquierda del panel de resultados, verás el número de eventos devueltos por tu búsqueda.
- **Zoom** ampliará el área del mapa de la Tierra donde se encuentra el evento.
- **Cola** agregará todos los resultados a las descargas, lo que te permite agregar todos los productos del evento a la cola de descarga.
	- Puedes optar por agregar **Todos los Productos del Evento** o **Productos del Evento Seleccionados** a la cola de descarga. Puedes seleccionar archivos individuales en la columna derecha.
- **Exportar** descargará el Script de Descarga a Granel. Este script en Python te permite descargar todos los productos de la escena seleccionada.
- **Bajo Demanda** te permitirá agregar todos los resultados a la cola de Bajo Demanda para procesamiento personalizado de las escenas. Dependiendo de los tipos de archivos asociados con el evento elegido, es posible que puedas agregar trabajos RTC o InSAR a tu cola. Para obtener más información, haz clic [aquí](https://hyp3-docs.asf.alaska.edu/using/vertex/).
- **Copiar** te permite copiar los **ID de Escena** o las **URL de Descarga**.
	- Puedes optar por copiar **Todos** los ID de Escena o URL, o solo copiar **ID de Escena o URL Seleccionados**. Puedes seleccionar archivos individuales en la columna derecha.
- La columna de Eventos (izquierda).
	- Cada evento tiene un ícono de terremoto o volcán a la izquierda para ayudarte a identificar rápidamente el tipo de evento.
	- Haz clic en **Zoom al Evento** para ampliar el área del mapa de la Tierra donde se encuentra el evento.
- La columna de Detalle del Evento (centro).
	- Los detalles del evento se enumeran aquí. Esto incluye el tiempo de inicio y finalización del procesamiento del evento. Para los terremotos, también se muestra la magnitud y la profundidad.
	- Puedes **Copiar** el ID del Evento.
	- Haz clic en **Evento SARVIEWS** para ser dirigido a la página SARVIEWS de tu evento elegido.
	- Para eventos de terremotos, se muestra el **ID del USGS**. Para los volcanes, se muestra el **ID del Smithsonian**. Haz clic en el enlace para ir a la página de eventos del USGS o del Smithsonian.
	- Ajusta el control deslizante de **Escala del Polígono de Búsqueda Geográfica** según lo desees. El polígono de Área de Interés también se actualizará en el mapa.
	- Una vez que estés satisfecho con la **Escala del Polígono de Búsqueda Geográfica**, haz clic en **Geográfica** para iniciar una búsqueda geográfica utilizando el Área de Interés y las fechas del evento.
	- Haz clic en **Lista** para iniciar una búsqueda de lista que incluye todas las escenas de productos del evento.
	- Haz clic en **SARVIEWS** para ser dirigido a la página SARVIEWS de tu evento elegido.

- El ícono del ojo etiquetado como **Abrir en Visor de Imágenes** abre una ventana de vista previa más grande.
    - *Nota*: Al ver imágenes InSAR en el visor de imágenes, se muestra la imagen de vista previa envuelta. La imagen de vista previa sin envolver está disponible en el producto descargado.
    - En el visor de vista previa, **amplía** usando los botones **+** o **-**. También puedes hacer zoom y panoramizar con el mouse.
    - Haz clic o desplázate por las miniaturas en la parte inferior para ver otras imágenes de vista previa para el evento seleccionado.
    - Los metadatos de la escena se enumeran en el lado derecho de la ventana del visor de vista previa.
    - Bajo **Archivo**, puedes hacer clic en el botón etiquetado **RTC GAMMA** o **INSAR GAMMA** para obtener más opciones.
        - Haz clic en **Descargar Archivo** para descargar el producto seleccionado.
        - Haz clic en **Agregar archivo a la cola** para agregarlo a tu cola de descarga.
        - Haz clic en **Escenas de Referencia** para copiar los nombres de las escenas de referencia al portapapeles. Estos pueden guardarse en un archivo o utilizarse en una **Búsqueda de Lista**.
        - Haz clic en **Anclar Vista Previa al Mapa** para anclar la imagen de vista previa al mapa. Una vez anclada, puedes hacer clic en este botón nuevamente para desanclarla.
    - Haz clic en el ícono **Descargar esta imagen** para descargar la imagen de vista previa.
    - Haz clic en el ícono **Anclar** para anclar la imagen de vista previa seleccionada al mapa. Una vez anclada, puedes hacer clic en este botón nuevamente para desanclarla.
- La columna de Archivos (derecha).
    - El número total de archivos para el evento seleccionado se muestra en esta columna.
    - Puedes ordenar los archivos usando los botones **Ordenar por** y **Orden** en la parte superior de la columna.
        - Bajo **Ordenar por**, puedes elegir **Fecha**, **Ruta** o **Cuadro**.
        - Haz clic en la **Flecha de Orden** para alternar entre orden ascendente y descendente.
    - Haz clic en **Criterios de Producto** para abrir los Filtros de Búsqueda.
    - Haz clic en las **casillas de verificación** junto a cada archivo para seleccionarlo o deseleccionarlo. Los archivos seleccionados se anclarán en el mapa. Una vez que hayas seleccionado los archivos deseados, también puedes usar los controles **Descargar** o **Copiar** en la parte superior izquierda del panel de resultados para interactuar con los productos seleccionados.
    - Haz clic en **Bajo Demanda** para agregar el archivo seleccionado a tu cola de Bajo Demanda para procesamiento adicional.
    - Haz clic en el ícono del **Carrito de Compras** para agregar el archivo seleccionado a tu cola de Descarga.
    - Haz clic en **Descargar** para descargar el archivo seleccionado.
    - *Nota*: Debes iniciar sesión para descargar productos.

